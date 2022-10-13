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

# Initialise empty graph G
G = graph.create_weighted_graph(5,5)

# Run your chosen algorithm and get a path back.
path = dijkstra.algorithm(G, 0, 18)
# path = a_star.algorithm(G, 0, 18)
# path = breadth_first.algorithm(G,0,18)
# path = list(depth_first.algorithm(G,0,18))
# path = list(bre.algorithm(G,0,18))
# path = list(bre.algorithm(G,0,18))


# Add path as edges to G
for i in range((len(path) - 1)):
    G[path[0+i]][path[1+i]]['color']="r"
    G[path[0+i]][path[1+i]]['thickness']=5

# Set vertex positioning to layers of straight lines
pos = nx.multipartite_layout(G, subset_key='layer')

# Plot graph
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()
thickness = nx.get_edge_attributes(G,'thickness').values()
labels = nx.get_edge_attributes(G,'weight')


plt.figure(figsize=(15, 10))
nx.draw(G, pos, node_size=1000, node_color='#43C3FF', with_labels=True, font_color='white', edge_color=colors, width=list(thickness))
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()