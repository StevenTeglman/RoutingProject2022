from util import graph
from algorithms import sdto
import matplotlib.pyplot as plt
import networkx as nx
import pprint

# G = graph.create_unweighted_multidigraph(5,5)
G = nx.read_gpickle("simulation_logs\\17_13_24_46\graph.gpickle")
start = 348
end = 1486
# graph.create_dangers(7,7,G)
# graph.create_dangers(5,5,G)
# graph.create_dangers(21,21,G)

# graph.create_obstacle(6, 16, 5, G)

# graph.create_disturbances_between_nodes(2,7,G)
# graph.create_disturbances_between_nodes(8,7,G)
# graph.create_disturbances_between_nodes(9,8,G)
# graph.create_disturbances_between_nodes(12,7,G)
# graph.create_disturbances_between_nodes(17,12,G)
# graph.create_disturbances_between_nodes(22,17,G)
# graph.create_disturbances_between_nodes(22,21,G)

G = sdto.algorithm(graph=G, start=start, end=end, safety_value_min=10, distance_saved_allowence=5)

pp = pprint.PrettyPrinter(indent=4, depth = 3, compact = True)
pp.pprint(G.nodes[start])
# print(G.nodes[0])
# region plotty mcplotface
## Set vertex positioning to layers of straight lines

pos = nx.multipartite_layout(G, subset_key='layer')

for node in G.nodes():
    sv = G.nodes[node]["safety_value"]
    heur = G.nodes[node]["heuristic"]
    label = f"Node: {node}\nSV: {sv}\nHeur: {heur}"
    G.nodes[node]['label'] = label

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
            


# plt.axis('off')
# plt.show()

# endregion