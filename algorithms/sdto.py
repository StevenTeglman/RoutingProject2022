# Safety Distance Trade-Off Algorithm. Let's go, gamers

from math import inf, isinf
from util import robustness

def backwards_dijkstra_path_collection(graph, end, safety_value_min):
    unvisited = list(graph)
    obstacles = [n for n,v in graph.nodes(data=True) if v['is_obstacle'] != False]
    for obstacle in obstacles:
        unvisited.remove(obstacle)
    
    leftover_infinity_nodes = []
    distances = {}
    graph.nodes[end]['color'] = 'darkseagreen'
    graph.nodes[end]['path_to_goal'] = [end]
    graph.nodes[end]['safety_value_paths'][safety_value_min] = [end]
    
    for node in unvisited:
        graph.nodes[node]['heuristic'] = inf
        distances[node] = inf
    
    distances[end] = 0

    while len(unvisited):
        current_node = None
        for node in unvisited:
            if current_node == None or distances[node] < distances[current_node]:
                current_node = node
                
        for neighbor in graph[current_node]:
            if graph.nodes[neighbor]["safety_value"] < safety_value_min:
                continue
            
            heuristic = distances[current_node] + graph[current_node][neighbor][0]['weight']
            if heuristic < distances[neighbor]:
                distances[neighbor] = heuristic
                graph.nodes[neighbor]["heuristic"] = heuristic
                
        lowest_heuristic = inf        
        lowest_heuristic_node = None
        unvisited.remove(current_node)
    
        if end != current_node:
            for neighbor in graph[current_node]:
                if distances[neighbor] < lowest_heuristic:
                    lowest_heuristic = distances[neighbor]
                    lowest_heuristic_node = neighbor
            path = [current_node]

            # Check if there are neighbors that can be traveled to
            if lowest_heuristic_node or lowest_heuristic_node == 0:
                graph.nodes[current_node]['safety_value_paths'][safety_value_min] = path + graph.nodes[lowest_heuristic_node]['safety_value_paths'][safety_value_min]
            
            else:                     
                graph.nodes[current_node]['safety_value_paths'][safety_value_min] = []
        
                
    for node in graph.nodes():
        if 'path_to_goal' in graph.nodes()[node]:
            if len(graph.nodes()[node]['path_to_goal']) > 1:
                graph.nodes()[node]['path_to_goal'] = graph.nodes()[node]['path_to_goal']
    
    for k, v in distances.items():
        if isinf(v):
            leftover_infinity_nodes.append(k)
                
    print(f"Infinity Nodes: {leftover_infinity_nodes}")
    return graph

def collect_safety_values(graph):
    safety_value_set = set()
    for node in graph.nodes():
        if not graph.nodes[node]['is_obstacle']:
            safety_value = graph.nodes()[node]['safety_value']
            safety_value_set.add(safety_value)
    
    if 0 in safety_value_set:
        safety_value_set.remove(0) 
    # safety_value_set.remove(inf)
    # safety_value_set.add(100)
    return list(safety_value_set)

def algorithm(graph, end, safety_value_min, distance_saved_allowence):
    graph = robustness.robustness_calculation(graph)
    
    # Collect Every unique safety value
    safety_values = collect_safety_values(graph)
    print(safety_values)
    # Check to see if user specified safety value in graph
    if safety_value_min not in safety_values:
        safety_values_copy = safety_values.copy()
        if inf in safety_values_copy:
            safety_values_copy.remove(inf)
        
        print(safety_values_copy)
        # Set safety_value_min to highest none inf value
        safety_values_copy.sort()
        safety_value_min = safety_values_copy[-1]
        
        print("\n#############################################")
        print("The chosen safety value is too high for graph")
        print(f"New Min Safety Value {safety_value_min}\n")

    for node in graph.nodes():  
        for safety_value in safety_values:
            graph.nodes[node]["safety_value_paths"][safety_value] = []
    
    # Collect path for every unique safety value
    for safety_value in safety_values:
        backwards_dijkstra_path_collection(graph, end, safety_value)
        
    # Computer the SDTO
    for node in graph.nodes():
        # If no path originally exists with defined safety value, return empty list

        if not graph.nodes[node]['safety_value_paths'][safety_value_min]:
            graph.nodes[node]['sdto_path'] = []
            print(f"No path exists for this node {node}")
            continue
        else:
            safety_value_length_pairs = {}
            for k,v in graph.nodes[node]['safety_value_paths'].items():
                safety_value_length_pairs[k] = len(v)

        # Check to ensure there exists a safety_value in the node beneath our sv_min so we can compare.
        # If no, current sv_path is just assigned to sdto_path
        if safety_value_min-1 in safety_value_length_pairs:
            difference_saved = safety_value_length_pairs[safety_value_min] - safety_value_length_pairs[safety_value_min-1]
            # If distance saved is greater or equal to distance saved allowence, assign the new path to that nodes SDTO path
            if difference_saved >= distance_saved_allowence:
                graph.nodes[node]['sdto_path'] = graph.nodes[node]['safety_value_paths'][safety_value_min-1]
            
            else:
                graph.nodes[node]['sdto_path'] = graph.nodes[node]['safety_value_paths'][safety_value_min]
        else:
            graph.nodes[node]['sdto_path'] = graph.nodes[node]['safety_value_paths'][safety_value_min]

        
    # Create paths out of previously unreachable nodes
    for node in graph.nodes():
        if not graph.nodes[node]['sdto_path'] and not graph.nodes[node]['is_danger'] and not graph.nodes[node]['is_obstacle']:
            print(node)
            safety_value_keys = []
            for k, v in graph.nodes[node]['safety_value_paths'].items():
                if v:
                    safety_value_keys.append(k)
            safety_value_keys.sort(reverse=True)
            print(safety_value_keys)

            # Find the highest safety_value with a path for that node
            # and assigns the corresponding path to sdto_path
            for svk in safety_value_keys:
                if svk:
                    graph.nodes[node]['sdto_path'] = graph.nodes[node]['safety_value_paths'][svk]
                    break
        
    return graph