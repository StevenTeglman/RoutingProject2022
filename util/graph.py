import math
import random
import networkx as nx
import numpy as np
import math

def create_unweighted_graph(x: int, y: int):
    # Initialise empty graph G
    G = nx.DiGraph()

    # Create 120 vertex labels
    vertices = np.arange(0, x*y, 1)

    # Reshape to emulate 12x10 crop patch
    layers = vertices.reshape((x, y))
    
    # Add vertices and edges to G
    for i in range(y):
        for j in range(x):
            v = layers[j][i]
            
            # For each vertex, store vertex label and layer/column position 0-11
            G.add_node(v, layer=i,color='#43C3FF', safety_value=math.inf)
            
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
        G[i[0]][i[1]]['thickness']=1
        G[i[0]][i[1]]['is_disturbance']=False
        G[i[0]][i[1]]['style']='solid'
        
        
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
            G.add_node(v, layer=i,color='#43C3FF', safety_value=math.inf)
            
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

def create_obstacle(x,y,step,graph):
        #find all neighbors of nodes between x and y
        for i in range(x,y+1,step):
            neighbors = graph.neighbors(i) 
            #remove edges connected to the obstacles
            for ne in list(neighbors):
                    graph.remove_edge(i,ne)

            #color the removed nodes(obstacles) black
            n=graph.nodes()        
            n[i]['color']='black'       

def create_dangers(start,end,graph,step=1):

        for i in range(start,end+1,step):

            #color the selected nodes and set safety to 0
            n=graph.nodes()
            n[i]['color']='red'
            n[i]['safety_value']=0

def create_disturbances_between_nodes(start, end, graph):
    graph[start][end]['is_disturbance']=True
    graph[start][end]['style']='dashed'


def graph_preset_1():
    G = create_unweighted_graph(10,10)
    create_obstacle(1,71,10,G)
    create_obstacle(32,35,1,G)
    create_obstacle(15,25,10,G)
    create_obstacle(36,37,1,G)
    create_obstacle(73,77,1,G)
    create_obstacle(87,97,10,G)
    create_obstacle(53,57,1,G)
    create_obstacle(58,88,10,G)
    return G

def graph_preset_2():
    G = create_unweighted_graph(10,10)
    create_obstacle(11,88,3,G)
    return G

def graph_preset_3():
    G = create_unweighted_graph(10,10)
    create_obstacle(10,90,10,G)
    create_obstacle(2,32,10,G)
    create_obstacle(52,92,10,G)
    create_obstacle(94,98,1,G)
    create_obstacle(56,86,10,G)
    create_obstacle(86,88,1,G)
    create_obstacle(56,78,10,G)
    create_obstacle(17,47,10,G)
    create_obstacle(47,48,1,G)
    create_obstacle(68,69,1,G)
    create_obstacle(3,33,10,G)
    create_obstacle(4,5,1,G)
    create_obstacle(15,35,10,G)
    create_obstacle(53,93,10,G)
    create_obstacle(54,54,1,G)
    create_obstacle(75,85,10,G)
    create_obstacle(9,29,10,G)
    return G

def graph_preset_4():
    G = create_unweighted_graph(10,10)
    create_dangers(0,9,G)
    create_disturbances_between_nodes(10,0,G)
    return G

def get_specific_manhattan(start, stop, graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist[start][stop]

def get_all_manhattan(graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist