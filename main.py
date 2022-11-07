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
G = graph.GraphPreset1(10)
#G = graph.GraphPreset2(10)
#G = graph.GraphPreset3(10)


#Run your chosen algorithm and get a path back.
#path, stats = dijkstra.algorithm(G, start, end)
path, stats = a_star.algorithm(G, start, end)
# path, stats = breadth_first.non_recursive_algorithm(G,start,end)
# path = list(depth_first.algorithm(G,start,end))
#path, stats = list(greedy_best_first.algorithm(G,start,end))


print(stats)
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
nodeColor = nx.get_node_attributes(G,'color').values()


plt.figure(figsize=(15, 10))
nx.draw(G, pos, node_size=1000, node_color=nodeColor, with_labels=True, font_color='white', edge_color=colors, width=list(thickness))
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()