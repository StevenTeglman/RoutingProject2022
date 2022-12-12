from util import graph, robustness, traverse_simulator
from algorithms import backwards_dijkstra

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
#print(G.nodes())

print(traverse_simulator.traverse(G, 24, 10))