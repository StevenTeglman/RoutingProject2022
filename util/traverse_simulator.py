import random

def traverse(graph, start, disturbance_chance):
    state = (True, start)
    current_node_index = start

    #print(current_node)
    while current_node_index != 4: # TODO: change to current_node_index != current_node['path_to_goal']
        current_node = graph.nodes()[current_node_index]
        # Set the destination of the current "step"
        predicted_index = current_node['path_to_goal'][1]
        
        if current_node['is_danger']:
            return (False, current_node_index)

        for edge in graph.edges(current_node_index, data=True):
            if edge[2]['is_disturbance']:
                get_disturbed = random.randint(1, 100) <= disturbance_chance
                if get_disturbed:
                    predicted_index = edge[1]
                    break
        
        current_node_index = predicted_index
        state = (True, current_node_index)
    return state
        
