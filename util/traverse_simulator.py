import random

def traverse(graph, start, disturbance_chance, sv_min):
    disturbance_counter = 0
    path = []
    is_alternative = graph.nodes[start]['is_sdto_alternative']
    distance_saved = None
    state = (False, path, disturbance_counter, is_alternative, distance_saved)
    current_node_index = start
    current_node = graph.nodes()[current_node_index]

    while len(current_node['sdto_path']) > 1:
        # Set the destination of the current "step"
        path.append(int(current_node_index))
        predicted_index = current_node['sdto_path'][1]

        if current_node['is_danger']:
            return (False, path, disturbance_counter, is_alternative, distance_saved)

        if current_node['is_sdto_alternative'] and not distance_saved:
            is_alternative = True
            if sv_min > 1:
                distance_saved = len(current_node["safety_value_paths"][sv_min]) - len(current_node["safety_value_paths"][sv_min-1]) 
        
        for edge in graph.edges(current_node_index, data=True):
            if edge[2]['is_disturbance']:
                get_disturbed = random.randint(1, 100) <= disturbance_chance
                if get_disturbed:
                    predicted_index = edge[1]
                    disturbance_counter += 1
        
        current_node_index = predicted_index
        if current_node_index == graph.nodes[start]['sdto_path'][-1]:
            state = (True, path, disturbance_counter, is_alternative, distance_saved)
        current_node = graph.nodes()[current_node_index]
    return state
        
