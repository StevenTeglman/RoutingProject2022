from util import graph, robustness, traverse_simulator
from algorithms import backwards_dijkstra
import datetime
import json

G = graph.create_unweighted_multidigraph(5,5)

graph.create_dangers(7,7,G)

graph.create_disturbances_between_nodes(6,7,G)
graph.create_disturbances_between_nodes(5,6,G)
graph.create_disturbances_between_nodes(11,6,G)
graph.create_disturbances_between_nodes(8,7,G)
graph.create_disturbances_between_nodes(12,7,G)
graph.create_disturbances_between_nodes(17,12,G)
graph.create_disturbances_between_nodes(22,17,G)

graph.create_obstacle(17,19,1,G)

robustness.robustness_calculation(G)

G = backwards_dijkstra.algorithm(G, 0, 4, 2)


def run_simulation(number_of_iterations, graph, start, disturbance_chance):
    result = {}
    _now = datetime.datetime.now()
    filename = f"{_now.day}_{_now.hour}_{_now.minute}_{_now.second}"

    for current_iteration in range(number_of_iterations):
        current_traversal = traverse_simulator.traverse(graph, start, disturbance_chance)
        result[current_iteration] = current_traversal

    with open(f"./simulation_logs/{filename}.json", "w") as file:
        json.dump(result, file, indent=None)


# print(traverse_simulator.traverse(G, 24, 60))
run_simulation(10, G, 24, 60)