import math
import random
import networkx as nx
import numpy as np
import math

def create_unweighted_multidigraph(x: int, y: int):
    # Initialise empty graph G
    G = nx.MultiDiGraph()

    # Create 120 vertex labels
    vertices = np.arange(0, x*y, 1)

    # Reshape to emulate 12x10 crop patch
    layers = vertices.reshape((x, y))
    
    # Add vertices and edges to G
    for i in range(y):
        for j in range(x):
            v = layers[j][i]
            
            # For each vertex, store vertex label and layer/column position 0-11
            G.add_node(v, layer=i,color='#43C3FF', safety_value=math.inf, is_obstacle=False)
            
            # For each vertex, store edge to each vertex
            # Right
            if i == y-1:
                pass
            else:
                G.add_edge(v, v+1, color="black",
                                    weight=1,
                                    thickness=1,
                                    is_disturbance=False,
                                    style="solid"
                                    )

            #Left
            if i == 0:
                pass
            else:
                G.add_edge(v, v-1, color="black",
                                    weight=1,
                                    thickness=1,
                                    is_disturbance=False,
                                    style="solid"
                                    )

            #Up
            if v < y:
                pass
            else:
                G.add_edge(v, v-y, color="black",
                                    weight=1,
                                    thickness=1,
                                    is_disturbance=False,
                                    style="solid"
                                    )

            #Down
            if v > layers[-2][-1]:
                pass
            else:
                G.add_edge(v, v+y, color="black",
                                    weight=1,
                                    thickness=1,
                                    is_disturbance=False,
                                    style="solid"
                                    )
    
    edges = G.edges()
    new_edges = []
    for edge in edges:
        node_from, node_to = edge
        new_node = (node_from, 
                    node_to,
                    0, 
    {"color":"black",
    "weight":1,
    "thickness":1,
    "is_disturbance":False,
    "style":"solid"
    }
                    )
        new_edges.append(new_node)
    G.update(new_edges)
    return G

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

def create_obstacle(start, end, step, graph):
        # Find all neighbors of nodes between start and end
        for i in range(start, end+1, step):
            edges = graph.edges(i) 
            # Remove edges connected to the obstacles
            for edge in list(edges):
                graph.remove_edge(edge[0],edge[1])
                while (edge[1], edge[0]) in graph.edges(edge[1]):
                    graph.remove_edge(edge[1],edge[0])

            # Color the removed nodes(obstacles) black
            n=graph.nodes()        
            n[i]['color']='black'       
            n[i]['is_obstacle']= True       

def create_dangers(start,end,graph,step=1):

        for i in range(start,end+1,step):

            #color the selected nodes and set safety to 0
            n=graph.nodes()
            n[i]['color']='red'
            n[i]['safety_value']=0

def create_disturbances_between_nodes(start, end, graph):
    new_node = (start, 
                end, 
                    {
                        "color":"black",
                        "weight":1,
                        "thickness":1,
                        "is_disturbance":True,
                        "style":'dashed'
                    }
                )
    new_edges = [new_node]
    graph.add_edges_from(new_edges)


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
    G = create_unweighted_multidigraph(10,10)
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
    G = create_unweighted_multidigraph(10,10)
    create_dangers(0,9,G)
    # Create 2 horizontal levels of disturbances pointing north.
    for i in range(0,10):
        create_disturbances_between_nodes(i+10, i, G)
        create_disturbances_between_nodes(i+20, i+10, G)
    create_obstacle(10,14,2,G)
    create_obstacle(20,24,1,G)
    return G

def graph_preset_5():
    G = create_unweighted_multidigraph(10,10)
    create_dangers(0,9,G)
    # Create 2 horizontal levels of disturbances pointing north.
    for i in range(0,10):
        create_disturbances_between_nodes(i+10, i, G)
        create_disturbances_between_nodes(i+20, i+10, G)
    create_disturbances_between_nodes(20, 21, G)
    return G

def graph_preset_6():
    G = create_unweighted_multidigraph(4,4)
    create_dangers(0,3,G)
    # Create 2 horizontal levels of disturbances pointing north.
    for i in range(0,4):
        create_disturbances_between_nodes(i+4, i, G)
        create_disturbances_between_nodes(i+8, i+4, G)
    return G

def get_specific_manhattan(start, stop, graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist[start][stop]

def get_all_manhattan(graph):
    dist = dict(nx.all_pairs_shortest_path_length(graph))
    return dist