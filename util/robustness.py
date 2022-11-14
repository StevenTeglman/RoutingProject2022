import math

def calculate_solid_safety_values(graph):
    # Get list of all 'non-infinity' nodes as nn
    # TODO Change this so that it isn't just looking for "non inf nodes"
    non_infinity_nodes = [node for node in graph.nodes() if graph.nodes[node]['safety_value'] != math.inf and not graph.nodes[node]['is_obstacle']]
    old_non_infinity_nodes =[]
    
    # iterate all nodes while non_infinity_nodes not equal last non_infinity_nodes
    while non_infinity_nodes != old_non_infinity_nodes:
        for node in graph.nodes():
            if graph.nodes[node]['is_obstacle']:
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
        
        old_non_infinity_nodes = non_infinity_nodes
        non_infinity_nodes = [node for node in graph.nodes() if graph.nodes[node]['safety_value'] != math.inf]
    
    return graph


def attractor(graph):
    # TODO Change this so that it isn't just looking for "non inf nodes", maybe?
    # Get list of all 'non-infinity' nodes as nn
    non_infinity_nodes = [node for node in graph.nodes() if graph.nodes[node]['safety_value'] != math.inf and not graph.nodes[node]['is_obstacle']]
    old_non_infinity_nodes =[]
    while non_infinity_nodes != old_non_infinity_nodes:
        for node in graph.nodes():
            if graph.nodes[node]['is_obstacle']:
                continue
            
            normal_edges = []
            disturbance_edges = []
            for edge in graph.edges(node, data=True):
                if not edge[2]["is_disturbance"]:
                    norm_edge = (edge[1], graph.nodes[edge[1]]["safety_value"])
                    normal_edges.append(norm_edge)
                else:
                    dist_edge = (edge[1], graph.nodes[edge[1]]["safety_value"])
                    disturbance_edges.append(dist_edge)
            #BUG All disturbance edges are inf and I don't know why...
            
            max_normal_edge = max(normal_edges, key=lambda tup: tup[1])
            # Check if there are actually disturbances
            if disturbance_edges:
                min_disturbance_edge = min(disturbance_edges, key=lambda tup: tup[1])
                
                min_disturbance_edge += (min_disturbance_edge[0],min_disturbance_edge[1] + 1)
                print("\nDisturbance, Max and min")
                print(disturbance_edges)
                print(max_normal_edge)
                print(min_disturbance_edge)
                min_safety_value = min([max_normal_edge, min_disturbance_edge], key=lambda tup: tup[1])[1]
            else:
                min_safety_value = max_normal_edge[1]
                           
            graph.nodes[node]["safety_value"] = min_safety_value
            
        old_non_infinity_nodes = non_infinity_nodes
        non_infinity_nodes = [node for node in graph.nodes() if graph.nodes[node]['safety_value'] != math.inf]
        # get max value of all normal edges
        # get min value +1 of all disturbance edges
        # get min value of both.
    
    return graph

        
    