import random

def traverse(graph, start, disturbance_chance):
    disturbance_counter = 0
    state = (True, start, disturbance_counter)
    current_node_index = start

    #print(current_node)
    while current_node_index != 4: # TODO: change to current_node_index != current_node['path_to_goal']
        current_node = graph.nodes()[current_node_index]
        # Set the destination of the current "step"
        predicted_index = current_node['path_to_goal'][1]
        
        if current_node['is_danger']:
            return (False, int(current_node_index), disturbance_counter)    # Had to cast as int since it returned as a numpy element

        for edge in graph.edges(current_node_index, data=True):
            if edge[2]['is_disturbance']:
                get_disturbed = random.randint(1, 100) <= disturbance_chance
                if get_disturbed:
                    predicted_index = edge[1]
                    disturbance_counter += 1
        
        current_node_index = predicted_index
        state = (True, current_node_index, disturbance_counter)
    return state
        
