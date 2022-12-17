from ast import List
import pprint
from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from util import graph, robustness
from algorithms import breadth_first
from algorithms import depth_first
from algorithms import dijkstra
from algorithms import a_star
from algorithms import greedy_best_first
from algorithms import sdto

## Initialise empty graph G
# G = graph.create_unweighted_multidigraph(50,50)
# start = int(input("Enter a number for the start node: "))
# end = int(input("Enter a number for the goal node: "))
start = 0
end = 2499
G = graph.graph_preset_1()
# G = graph.graph_preset_2()
# G = graph.graph_preset_3()
G = graph.graph_preset_4()
G = nx.read_gpickle("./simulation_logs/17_11_54_43/graph.gpickle")
# G = robustness.robustness_calculation(G)

G = sdto.algorithm(G, 2488, 335, 2, 2)

pp = pprint.PrettyPrinter(indent=4, depth = 3, compact = True)
pp.pprint(G.nodes[335])
## Run your chosen algorithm and get a path back.
# path, stats = dijkstra.algorithm(G, start, end)
# path, stats = a_star.algorithm(G, start, end)
# path, stats = breadth_first.non_recursive_algorithm(G,start,end)
# path,stats = list(depth_first.algorithm(G,start,end))
# path, stats = list(greedy_best_first.algorithm(G,start,end))
# path, stats = a_star.algorithm2(G, start, end)


# print(path, stats)

# region Creating figure plotting things

## Add path as edges to G
# for e in G.edges:
#     for i in range((len(path) - 1)):
#         G[path[0+i]][path[1+i]][e[2]]['color']="g"
#         G[path[0+i]][path[1+i]][e[2]]['thickness']=1.5
# for node in path:
#     G.nodes[node]['color'] = 'g'

# G.nodes[path[0]]['color'] = 'darkblue'
# G.nodes[path[-1]]['color'] = 'darkseagreen'


## Set vertex positioning to layers of straight lines

pos = nx.multipartite_layout(G, subset_key='layer')

## Plot graph
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()
thickness = nx.get_edge_attributes(G,'thickness').values()
labels = nx.get_edge_attributes(G,'weight')
node_color = nx.get_node_attributes(G,'color').values()
node_label = nx.get_node_attributes(G,'safety_value')
edge_style = nx.get_edge_attributes(G,'style').values()


plt.figure(figsize=(50,50))

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
                        font_color='white',
                        labels=node_label)
            

# plt.savefig('graph.svg', dpi = 1000)
# plt.axis('off')
# plt.show()

# endregion