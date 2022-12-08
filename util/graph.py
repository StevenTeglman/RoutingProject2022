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
            G.add_node(v, layer=i,color='#43C3FF', safety_value=math.inf, is_obstacle=False, is_danger=False)
            
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
            n[i]['color']='white'       
            n[i]['is_obstacle']= True       
            n[i]['is_danger']= False       
            n[i]['heuristic']= math.inf       

def create_dangers(start,end,graph,step=1):

        for i in range(start,end+1,step):

            #color the selected nodes and set safety to 0
            n=graph.nodes()
            n[i]['color']='red'
            n[i]['safety_value']=0
            n[i]['is_danger']=True

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

def graph_random(grid_size, wind_direction='up'):
    G = create_unweighted_multidigraph(grid_size,grid_size)

    wind_position = 0

    #create_dangers(0,size_x-1,G)

    # Create 2 horizontal levels of disturbances pointing north.
    #for i in range(0,size_x):
    #    create_disturbances_between_nodes(i+size_x, i, G)
    #    create_disturbances_between_nodes(i+(size_x*2), i+size_x, G)
   
    all_nodes = G.nodes()
    obstacle_nodes = []
    danger_nodes = []
    for node in all_nodes:
        is_danger_node = random.randint(0, int(grid_size/2)) == 0
        if is_danger_node: 
            create_dangers(node, node, G)
            danger_nodes += [node]
        if node not in obstacle_nodes and all_nodes[node]['safety_value'] != 0:
            is_obstacle_origin = random.randint(0, grid_size-1) <= 1 
            if(is_obstacle_origin):
                obstacle_length = random.randint(1, 3)
                #print(obstacle_nodes)
                create_obstacle(node, (node+obstacle_length)-1, 1, G)
                obstacle_nodes += [i for i in range(node, node + obstacle_length)]
                
    obstacle_nodes_set = set(obstacle_nodes)
    danger_nodes_set = set(danger_nodes)
    all_nodes_set = set(all_nodes)
    non_obstacle_nodes = list(all_nodes_set.difference(obstacle_nodes_set))
    non_obstacle_danger_nodes = list(set(non_obstacle_nodes).difference(danger_nodes_set))
    for non_obstacle_danger_node in non_obstacle_danger_nodes:
        has_wind_blowing = random.randint(0, 2) == 0
        if has_wind_blowing:
            wind_target_node = -1
            if(wind_direction == 'up'):
                wind_target_node = non_obstacle_danger_node - grid_size
            elif(wind_direction == 'down'):
                wind_target_node = non_obstacle_danger_node + grid_size
            elif(wind_direction == 'left'):
                is_left_edge = non_obstacle_danger_node % grid_size == 0
                if not is_left_edge: wind_target_node = non_obstacle_danger_node - 1
            elif(wind_direction == 'right'):
                is_right_edge = non_obstacle_danger_node % grid_size == grid_size - 1
                if not is_right_edge: wind_target_node = non_obstacle_danger_node + 1
            

            if wind_target_node in non_obstacle_nodes:
                create_disturbances_between_nodes(non_obstacle_danger_node, wind_target_node, G)
    #create_obstacle(10,14,2,G)
    return G

def graph_preset_1():
    G = create_unweighted_multidigraph(50,50)
    create_obstacle(1,2200,50,G)
    create_obstacle(2201,2210,1,G)
    create_obstacle(10,1100,50,G)
    create_obstacle(1110,1120,1,G)
    create_obstacle(1360,2210,50,G)
    create_obstacle(820,1120,50,G)
    create_obstacle(820,840,1,G)
    create_obstacle(1360,1390,1,G)
    create_obstacle(2380,2495,50,G)
    create_obstacle(2385,2495,50,G)
    create_obstacle(2366,2380,1,G)
    create_obstacle(2166,2316,50,G)
    create_obstacle(2166,2188,1,G)
    create_obstacle(1788,2188,50,G)
    create_obstacle(1764,1788,1,G)
    create_obstacle(1613,1763,50,G)
    create_obstacle(1613,1644,1,G)
    create_obstacle(1694,2490,50,G)
    create_obstacle(2386,2390,1,G)
    create_obstacle(49,2498,50,G)
    return G

def graph_preset_2():
    G = create_unweighted_multidigraph(50,50)
    create_obstacle(2,500,4,G)
    create_obstacle(505,2497,4,G)
    create_obstacle(90,2499,10,G)
    return G

def graph_preset_3():
    G = create_unweighted_multidigraph(50,50)
    create_obstacle(10,2455,10,G)
    create_obstacle(2,750,10,G)
    create_obstacle(1252,2492,10,G)
    create_obstacle(2493,2498,1,G)
    create_obstacle(1255,2350,10,G)
    create_obstacle(70,140,10,G)
    create_obstacle(5,1500,10,G)
    create_obstacle(800,1100,10,G)
    return G

def graph_preset_4():
    G = create_unweighted_multidigraph(50,50)
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