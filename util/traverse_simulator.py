import random

def traverse(graph, start, disturbance_chance):
    disturbance_counter = 0
    path = [int(start)]
    is_alternative = graph.nodes[start]['is_sdto_alternative']
    state = (True, path, disturbance_counter, is_alternative)
    current_node_index = start
    current_node = graph.nodes()[current_node_index]

    while len(current_node['sdto_path']) > 1:
        # Set the destination of the current "step"
        path.append(int(current_node_index))
        predicted_index = current_node['sdto_path'][1]

        if  is_alternative == False:
            is_alternative = current_node['is_sdto_alternative']
        
        if current_node['is_danger']:
            return (False, path, disturbance_counter, is_alternative)

        for edge in graph.edges(current_node_index, data=True):
            if edge[2]['is_disturbance']:
                get_disturbed = random.randint(1, 100) <= disturbance_chance
                if get_disturbed:
                    predicted_index = edge[1]
                    disturbance_counter += 1
        
        current_node_index = predicted_index
        state = (True, path, disturbance_counter, is_alternative)
        current_node = graph.nodes()[current_node_index]
    return state
        
