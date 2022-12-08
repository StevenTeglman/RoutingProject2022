from ast import List
import math
import os
from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from algorithms.a_star import algorithm2
from util import graph, robustness
from algorithms import depth_first
import pickle
from algorithms import backwards_dijkstra

# Initialise empty graph G
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
os.system('cls')
print(f"Path to success: {G.nodes[24]['path_to_goal']}")

for node in G.nodes():
    sv = G.nodes[node]["safety_value"]
    heur = G.nodes[node]["heuristic"]
    label = f"Node: {node}\nSV: {sv}\nHeur: {heur}"
    G.nodes[node]['label'] = label
    
pos = nx.multipartite_layout(G, subset_key='layer')

## Plot graph
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()
thickness = nx.get_edge_attributes(G,'thickness').values()
labels = nx.get_edge_attributes(G,'weight')
node_color = nx.get_node_attributes(G,'color').values()
node_label = nx.get_node_attributes(G,'label')
edge_style = nx.get_edge_attributes(G,'style').values()

plt.figure(figsize=(10,10))

ax = plt.gca()
for e in G.edges:
     edge_style = G[e[0]][e[1]][e[2]]['style']
     color = G[e[0]][e[1]][e[2]]['color']
     ax.annotate("",
                    xy=pos[e[0]], xycoords='data',
                    xytext=pos[e[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="<-",
                                   shrinkA=-15, shrinkB=-15,
                                   patchA=None, patchB=None,
                                   connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2]+0.2)),
                                   edgecolor=color,
                                   linestyle=edge_style,
                                   linewidth=1,
                              
                              ),
                )

nx.draw_networkx_nodes(G,
                    pos,
                    node_size=750,
                    node_color=node_color)

nx.draw_networkx_labels(G,
                        pos,
                        font_color='black',
                        labels=node_label)
            

# plt.savefig('graph.svg', dpi = 1000)
plt.axis('off')
plt.show()