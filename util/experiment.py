from math import inf
from util.robustness import robustness_calculation
from util.traverse_simulator import traverse
from algorithms.sdto import algorithm as sdto
from algorithms.sdto import collect_safety_values
from util.graph import graph_random 
from datetime import datetime
import json
import os



def run_experiment(number_of_iterations=10, safety_value_min=2, disturbance_chance=25):
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
    _now = datetime.now()
    foldername = f"{_now.day}_{_now.hour}_{_now.minute}_{_now.second}"
    os.mkdir(f"./simulation_logs/{foldername}")

    while sv_min <= sv_max:
        G = sdto(G, end, sv_min, distance_saved_allowance)
        for current_iteration in range(number_of_iterations):
            current_traversal = traverse(G, start, disturbance_chance)
            traversal_data_num_only = [current_traversal[0], len(current_traversal[1]), current_traversal[2]]
            traversal_data_readable = [f"Goal reached: {current_traversal[0]}", f"Path length: {len(current_traversal[1])}", f"Times disturbed: {current_traversal[2]}"]
            result[current_iteration] = traversal_data_readable
            
        filename = f"SVmin{sv_min}_DSA{distance_saved_allowance}"
        with open(f"./simulation_logs/{foldername}/{filename}.json", "w") as file:
            json.dump(result, file, indent=4)

        result = {}
        sv_min += 1
