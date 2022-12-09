import math

def calculate_edge_values(graph):
    for node in graph.nodes():
        if graph.nodes[node]['is_obstacle'] or graph.nodes[node]['is_danger']:
            continue
        current_node_safety = graph.nodes[node]['safety_value']
        max_safety_value = 0
        
        # assign node max safety value of all neighbors
        for neighbor in graph.neighbors(node):
            neighbor_safety = graph.nodes[neighbor]['safety_value']
            if neighbor_safety > max_safety_value:
                max_safety_value = neighbor_safety
        
        if max_safety_value < current_node_safety:
            graph.nodes[node]['safety_value'] = max_safety_value

    return graph        



def calculate_disturbance_values(graph):
    for node in graph.nodes():
        if graph.nodes[node]['is_obstacle'] or graph.nodes[node]['is_danger']:
            continue
        
        normal_edges = []
        disturbance_edges = []
        for edge in graph.edges(node, data=True):
            # get all edges
            if not edge[2]["is_disturbance"]:
                norm_edge = (edge[1], graph.nodes[edge[1]]["safety_value"])
                normal_edges.append(norm_edge)
            # get all disturbance edges
            else:
                dist_edge = (edge[1], graph.nodes[edge[1]]["safety_value"])
                disturbance_edges.append(dist_edge)
                
        # Get Max Edge
        max_normal_edge = max(normal_edges, key=lambda tup: tup[1])
        
        # Check if there are actually disturbances. If not, go to next node
        if disturbance_edges:
            
            # Get min of all distances and increase value by one.
            min_disturbance_edge = min(disturbance_edges, key=lambda tup: tup[1])
            min_disturbance_edge = (min_disturbance_edge[0],min_disturbance_edge[1] + 1)
            
            # Get final safety value for node
            min_safety_value = min([max_normal_edge, min_disturbance_edge], key=lambda tup: tup[1])[1]
        else:
            continue
                        
        graph.nodes[node]["safety_value"] = min_safety_value
    return graph        

def robustness_calculation(graph):
    comparison_nodes = [(node, graph.nodes[node]['safety_value']) for node in graph.nodes() if graph.nodes[node]['safety_value'] != math.inf and not graph.nodes[node]['is_obstacle']]
    old_comparison_nodes =[]
    while comparison_nodes != old_comparison_nodes:    
        graph = calculate_edge_values(graph)
        graph = calculate_disturbance_values(graph)
        old_comparison_nodes = comparison_nodes
        comparison_nodes = [(node, graph.nodes[node]['safety_value']) for node in graph.nodes() if graph.nodes[node]['safety_value'] != math.inf]
    
    return graph