from util import graph
from algorithms import sdto
import matplotlib.pyplot as plt
import networkx as nx

G = graph.create_unweighted_multidigraph(4,4)

graph.create_dangers(5,5,G)
graph.create_disturbances_between_nodes(9,5,G)
graph.create_disturbances_between_nodes(6,5,G)
graph.create_disturbances_between_nodes(1,5,G)
graph.create_disturbances_between_nodes(4,5,G)
graph.create_disturbances_between_nodes(7,6,G)
G = sdto.algorithm(G, 15, 2, 0)

print(G.nodes[0])
# region plotty mcplotface
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
                        font_color='white',
                        labels=node_label)
            


plt.axis('off')
plt.show()

# endregion