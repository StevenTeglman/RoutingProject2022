from math import inf
import math
from util.robustness import robustness_calculation
from util.traverse_simulator import traverse
from algorithms.sdto import algorithm as sdto
from algorithms.sdto import collect_safety_values
from util.graph import graph_random 
from datetime import datetime
import pandas
import networkx
import random
import os



def run_experiment(number_of_iterations=200, safety_value_min=1, disturbance_chance=20):
    # Create a random graph for the experiment and select start/end nodes
    (G, eligible_nodes) = graph_random(75, disturbance_direction='random', disturbance_chance_percentage=55, obstacle_origin_chance=5, danger_scale=0.20)
    only_infs = [eligible_node for eligible_node in eligible_nodes if G.nodes[eligible_node]["safety_value"] == math.inf]
    start = random.choice(only_infs)
    eligible_nodes.remove(start)
    end = random.choice(eligible_nodes)

    G = sdto(G, end, start, 1, 2)
    if G.nodes[start]['sdto_path'] == []:
        return
    
    sv_min = safety_value_min
    safety_list = collect_safety_values(G)
    safety_list.remove(inf)
    sv_max = max(safety_list)
    allowances = [2, 5, 10]
    result = {}
    dict_keys = 0
    
    # Create a folder for the current experiment
    _now = datetime.now()
    foldername = f"{_now.day}_{_now.hour}_{_now.minute}_{_now.second}"
    os.mkdir(f"./simulation_logs/{foldername}")
   
    # Save current graph in the folder
    networkx.write_gpickle(G, f"./simulation_logs/{foldername}/graph.gpickle")

    # Save the list of eligible nodes as a text file
    with open(f"./simulation_logs/{foldername}/start_goal.txt", "w") as file:
        file.write(f"{start}, {end}")

    # Traverse the graph for every safety value, @number_of_iterations amount of times
    while sv_min <= sv_max:
        for allowance in allowances:
            G = sdto(G, end, start, sv_min, allowance)
            for current_iteration in range(number_of_iterations):
                current_traversal = traverse(G, start, disturbance_chance)
                result[dict_keys] = [
                                    current_traversal[0], 
                                    len(current_traversal[1]), 
                                    current_traversal[2], 
                                    current_traversal[3], 
                                    sv_min, 
                                    allowance,
                                    safety_list, 
                                    foldername
                                    ]
                dict_keys += 1
            
        sv_min += 1
    
    # Convert the results into a data frame, set column names, save as a csv file
    data_frame = pandas.DataFrame.from_dict(result, orient="index", 
                                            columns=[
                                                "goal_reached", 
                                                "path_length", 
                                                "times_disturbed", 
                                                "is_alternative", 
                                                "safety_value", 
                                                "allowance",
                                                "safety_list", 
                                                "graph_reference"
                                                ])
    data_frame.to_csv(f"./simulation_logs/{foldername}/data.csv")
