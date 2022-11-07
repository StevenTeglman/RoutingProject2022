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
            G.add_node(v, layer=i,color='#43C3FF')
            
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
            G.add_node(v, layer=i,color='#43C3FF')
            
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
        G[i[0]][i[1]]['thickness']= 2
        
        
    return G

def CreateObstacles(x,y,step,graph):
        #find all neighbors of nodes between x and y
        for i in range(x,y+1,step):
            neighbors = graph.neighbors(i) 
            #remove edges connected to the obstacles
            for ne in list(neighbors):
                    graph.remove_edge(i,ne)

            #color the removed nodes(obstacles) black
            n=graph.nodes()        
            n[i]['color']='black'       




def GraphPreset1(n):
    G = create_unweighted_graph(n,n)
    CreateObstacles(1,71,10,G)
    CreateObstacles(32,35,1,G)
    CreateObstacles(15,25,10,G)
    CreateObstacles(36,37,1,G)
    CreateObstacles(73,77,1,G)
    CreateObstacles(87,97,10,G)
    CreateObstacles(53,57,1,G)
    CreateObstacles(58,88,10,G)
    return G

def GraphPreset2(n):
    G = create_unweighted_graph(n,n)
    CreateObstacles(11,88,3,G)
    return G

def GraphPreset3(n):
    G = create_unweighted_graph(n,n)
    CreateObstacles(10,90,10,G)
    CreateObstacles(2,32,10,G)
    CreateObstacles(52,92,10,G)
    CreateObstacles(94,98,1,G)
    CreateObstacles(56,86,10,G)
    CreateObstacles(86,88,1,G)
    CreateObstacles(56,78,10,G)
    CreateObstacles(17,47,10,G)
    CreateObstacles(47,48,1,G)
    CreateObstacles(68,69,1,G)
    CreateObstacles(3,33,10,G)
    CreateObstacles(4,5,1,G)
    CreateObstacles(15,35,10,G)
    CreateObstacles(53,93,10,G)
    CreateObstacles(54,54,1,G)
    CreateObstacles(75,85,10,G)
    CreateObstacles(9,29,10,G)
    return G



def get_specific_manhattan(start, stop, graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist[start][stop]

def get_all_manhattan(graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist