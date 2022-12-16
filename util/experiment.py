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
    (G, eligible_nodes) = graph_random(35, disturbance_direction='up', disturbance_chance_percentage=75, obstacle_origin_chance=5)
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
    _now = datetime.now()
    foldername = f"{_now.day}_{_now.hour}_{_now.minute}_{_now.second}"
    os.mkdir(f"./simulation_logs/{foldername}")
    networkx.write_gpickle(G, f"./simulation_logs/{foldername}/graph.gpickle")

    while sv_min <= sv_max:
        G = sdto(G, end, sv_min, distance_saved_allowance)
        for current_iteration in range(number_of_iterations):
            current_traversal = traverse(G, start, disturbance_chance)
            traversal_data_num_only = [current_traversal[0], len(current_traversal[1]), current_traversal[2], sv_min]
            traversal_data_readable = [f"Goal reached: {current_traversal[0]}", f"Path length: {len(current_traversal[1])}", f"Times disturbed: {current_traversal[2]}", f"Safety Value: {sv_min}"]
            result[dict_keys] = traversal_data_num_only
            dict_keys += 1
            
        sv_min += 1
    
    data_frame = pandas.DataFrame.from_dict(result, orient="index", 
                                            columns=["goal_reached", "path_length", "times_disturbed", "safety_value"])
    data_frame.to_csv(f"./simulation_logs/{foldername}/data.csv")
