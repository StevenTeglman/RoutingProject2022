from util import graph, robustness, traverse_simulator
from turtle import color
from algorithms import sdto
import networkx as nx
import matplotlib.pyplot as plt
import datetime
import json

(G, eligible_nodes) = graph.graph_random(15, disturbance_direction='up', disturbance_chance_percentage=40, obstacle_origin_chance=5)
start = eligible_nodes[0]
end = eligible_nodes[-1]

G = robustness.robustness_calculation(G)

G = sdto.algorithm(G, end, 2, 2)

(state, path) = traverse_simulator.traverse(G, start, 50)

print('actual path', path)

for node in G.nodes():
    sv = G.nodes[node]["safety_value"]
    heur = G.nodes[node]["heuristic"]
    label = f"Node: {node}\nSV: {sv}\nHeur: {heur}"
    G.nodes[node]['label'] = label

# for e in G.edges:
#     for i in range((len(path) - 1)):
#         print(G.edges[path])
#         G.edges[path[0+i]][path[1+i]][e[2]]['color']="g"
#         G.edges[path[0+i]][path[1+i]][e[2]]['thickness']=1.5

for node in G.nodes()[start]['sdto_path']:
    G.nodes[node]['color'] = 'orange'

for node in path:
    G.nodes[node]['color'] = 'yellow'


if len(path) != 0:
    G.nodes[path[0]]['color'] = 'darkblue'
    G.nodes[path[-1]]['color'] = 'darkseagreen'

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



def run_simulation(number_of_iterations, graph, start, disturbance_chance):
    result = {}
    _now = datetime.datetime.now()
    filename = f"{_now.day}_{_now.hour}_{_now.minute}_{_now.second}"

    for current_iteration in range(number_of_iterations):
        current_traversal = traverse_simulator.traverse(graph, start, disturbance_chance)
        result[current_iteration] = current_traversal

    with open(f"./simulation_logs/{filename}.json", "w") as file:
        json.dump(result, file, indent=None)