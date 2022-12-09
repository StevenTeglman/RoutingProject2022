from math import inf, isinf

def algorithm(graph, start, end, safe_value_min):
    unvisited = list(graph)
    obstacles = [n for n,v in graph.nodes(data=True) if v['is_obstacle'] != False]
    for obstacle in obstacles:
        unvisited.remove(obstacle)
    
    distances = {}
    graph.nodes[end]['color'] = 'darkseagreen'
    graph.nodes[end]['path_to_goal'] = [end]
    
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
            if graph.nodes[neighbor]["safety_value"] < safe_value_min:
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
            graph.nodes[current_node]["path_to_goal"] = path + graph.nodes[lowest_heuristic_node]["path_to_goal"]
    
    for node in graph.nodes():
        if 'path_to_goal' in graph.nodes()[node]:
            if len(graph.nodes()[node]['path_to_goal']) > 1:
                graph.nodes()[node]['path_to_goal'] = graph.nodes()[node]['path_to_goal']

    return graph

def collect_safety_values(graph):
    safety_value_set = set()
    for node in graph.nodes():
        safety_value = graph.nodes()[node]['safety_value']
        safety_value_set.add(safety_value)
    
    safety_value_set.remove(0)
    return list(safety_value_set)

