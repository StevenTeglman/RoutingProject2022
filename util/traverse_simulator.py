import random

def traverse(graph, start, disturbance_chance):
    disturbance_counter = 0
    path = [int(start)]
    state = (True, path, disturbance_counter)
    current_node_index = start
    current_node = graph.nodes()[current_node_index]
    #print(current_node)
    while len(current_node['sdto_path']) > 1:       
        # Set the destination of the current "step"
        path.append(int(current_node_index))
        predicted_index = current_node['sdto_path'][1]  
        if current_node['is_danger']:
            return (False, path, disturbance_counter)

        for edge in graph.edges(current_node_index, data=True):
            if edge[2]['is_disturbance']:
                get_disturbed = random.randint(1, 100) <= disturbance_chance
                if get_disturbed:
                    predicted_index = edge[1]
                    disturbance_counter += 1
        
        current_node_index = predicted_index
        state = (True, path, disturbance_counter)
        current_node = graph.nodes()[current_node_index]
    return state
        
