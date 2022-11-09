from ast import List
from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from util import graph
from algorithms import breadth_first
from algorithms import depth_first
from algorithms import dijkstra
from algorithms import a_star
from algorithms import greedy_best_first

# Initialise empty graph G
#G = graph.create_weighted_graph(5,5)
start = int(input("Enter a number for the start node: "))
end = int(input("Enter a number for the goal node: "))
G = graph.graph_preset_4()
#G = graph.graph_preset_2()
#G = graph.graph_preset_3()


#Run your chosen algorithm and get a path back.
#path, stats = dijkstra.algorithm(G, start, end)
# path, stats = a_star.algorithm(G, start, end)
# path, stats = breadth_first.non_recursive_algorithm(G,start,end)
# path = list(depth_first.algorithm(G,start,end))
path, stats = list(greedy_best_first.algorithm(G,start,end))


print(stats)
# Add path as edges to G
for i in range((len(path) - 1)):
    G[path[0+i]][path[1+i]]['color']="g"
    G[path[0+i]][path[1+i]]['thickness']=1.5

# Set vertex positioning to layers of straight lines
pos = nx.multipartite_layout(G, subset_key='layer')

# Plot graph
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()
thickness = nx.get_edge_attributes(G,'thickness').values()
labels = nx.get_edge_attributes(G,'weight')
node_color = nx.get_node_attributes(G,'color').values()
node_label = nx.get_node_attributes(G,'safety_value')
edge_style = nx.get_edge_attributes(G,'style').values()


plt.figure(figsize=(40, 40))

nx.draw_networkx_nodes(G,
                    pos,
                    node_size=750,
                    node_color=node_color)

nx.draw_networkx_edges(G,
                    pos,
                    width=list(thickness),
                    edge_color=colors,
                    connectionstyle="arc3,rad=0.2",
                    style=list(edge_style),
                    arrows=True,
                    arrowsize=10,
                    arrowstyle='->',
                    node_size=750)

nx.draw_networkx_labels(G,
                        pos,
                        font_color='white',
                        labels=node_label)
plt.show()