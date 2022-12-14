import random

def traverse(graph, start, disturbance_chance):
    state = (True, start)
    path = []
    current_node_index = start
    current_node = graph.nodes()[current_node_index]
    #print(current_node)
    while len(current_node['sdto_path']) > 1: # TODO: change to current_node_index != current_node['path_to_goal']       
        # Set the destination of the current "step"
        path.append(current_node_index)
        predicted_index = current_node['sdto_path'][1]  
        if current_node['is_danger']:
            return (False, path)

        for edge in graph.edges(current_node_index, data=True):
            if edge[2]['is_disturbance']:
                get_disturbed = random.randint(1, 100) <= disturbance_chance
                if get_disturbed:
                    predicted_index = edge[1]
                    break
        
        current_node_index = predicted_index
        state = (True, path)
        current_node = graph.nodes()[current_node_index]
    return (state, path)
        
