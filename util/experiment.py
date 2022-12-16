from math import inf
from util.robustness import robustness_calculation
from util.traverse_simulator import traverse
from algorithms.sdto import algorithm as sdto
from algorithms.sdto import collect_safety_values
from util.graph import graph_random 
from datetime import datetime
import pandas
import networkx 
import os



def run_experiment(number_of_iterations=100, safety_value_min=1, disturbance_chance=25):
    # Create a random graph for the experiment and select start/end nodes
    (G, eligible_nodes) = graph_random(15, disturbance_direction='up', disturbance_chance_percentage=75, obstacle_origin_chance=5)
    start = eligible_nodes[0]
    end = eligible_nodes[-1]
    G = robustness_calculation(G)

    sv_min = safety_value_min
    safety_list = collect_safety_values(G)
    safety_list.remove(inf)
    sv_max = max(safety_list)
    distance_saved_allowance = 2
    result = {}
    dict_keys = 0
    
    # Create a folder for the current experiment
    _now = datetime.now()
    foldername = f"{_now.day}_{_now.hour}_{_now.minute}_{_now.second}"
    os.mkdir(f"./simulation_logs/{foldername}")
   
    # Save current graph in the folder
    networkx.write_gpickle(G, f"./simulation_logs/{foldername}/graph.gpickle")

    # Save the list of eligible nodes as a text file
    with open(f"./simulation_logs/{foldername}/eligible_nodes.txt", "w") as file:
        for line in eligible_nodes:
            file.write(f"{line}\n")

    # Traverse the graph for every safety value, @number_of_iterations amount of times
    while sv_min <= sv_max:
        G = sdto(G, end, start, sv_min, distance_saved_allowance)
        for current_iteration in range(number_of_iterations):
            current_traversal = traverse(G, start, disturbance_chance)
            traversal_data_num_only = [current_traversal[0], len(current_traversal[1]), current_traversal[2], current_traversal[3], sv_min, foldername]
            result[dict_keys] = traversal_data_num_only
            dict_keys += 1
            
        sv_min += 1
    
    # Convert the results into a data frame, set column names, save as a csv file
    data_frame = pandas.DataFrame.from_dict(result, orient="index", 
                                            columns=["goal_reached", "path_length", "times_disturbed", "is_alternative", "safety_value", "graph_reference"])
    data_frame.to_csv(f"./simulation_logs/{foldername}/data.csv")
