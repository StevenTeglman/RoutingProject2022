import random
import networkx as nx
import numpy as np

def create_unweighted_graph(x: int, y: int):
    # Initialise empty graph G
    G = nx.Graph()

    # Create 120 vertex labels
    vertices = np.arange(0, x*y, 1)

    # Reshape to emulate 12x10 crop patch
    layers = vertices.reshape((x, y))
    
    # Add vertices and edges to G
    for i in range(y):
        for j in range(x):
            v = layers[j][i]
            
            # For each vertex, store vertex label and layer/column position 0-11
            G.add_node(v, layer=i)
            
            # For each vertex, store edge to each vertex
            # Right
            if i == y-1:
                pass
            else:
                G.add_edge(v, v+1)

            #Left
            if i == 0:
                pass
            else:
                G.add_edge(v, v-1)

            #Up
            if v < y:
                pass
            else:
                G.add_edge(v, v-y)

            #Down
            if v > layers[-2][-1]:
                pass
            else:
                G.add_edge(v, v+y)
    
    e = G.edges()
    for i in e:
        G[i[0]][i[1]]['color']="black"
        G[i[0]][i[1]]['weight']=1
        
    return G

def create_weighted_graph(x: int, y: int):
    # Initialise empty graph G
    G = nx.Graph()

    # Create 120 vertex labels
    vertices = np.arange(0, x*y, 1)

    # Reshape to emulate 12x10 crop patch
    layers = vertices.reshape((x, y))
    
    # Add vertices and edges to G
    for i in range(y):
        for j in range(x):
            v = layers[j][i]
            
            # For each vertex, store vertex label and layer/column position 0-11
            G.add_node(v, layer=i)
            
            # For each vertex, store edge to each vertex
            # Right
            if i == y-1:
                pass
            else:
                G.add_edge(v, v+1)

            #Left
            if i == 0:
                pass
            else:
                G.add_edge(v, v-1)

            #Up
            if v < y:
                pass
            else:
                G.add_edge(v, v-y)

            #Down
            if v > layers[-2][-1]:
                pass
            else:
                G.add_edge(v, v+y)
    
    e = G.edges()
    for i in e:
        G[i[0]][i[1]]['color']="black"
        weight = random.randrange(1, 10)
        G[i[0]][i[1]]['weight']= weight
        G[i[0]][i[1]]['thickness']= weight
        
    return G

def get_specific_manhattan(start, stop, graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist[start][stop]

def get_all_manhattan(graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist