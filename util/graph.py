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
            G.add_node(v, 
                       layer=i,
                       color='#43C3FF', 
                       safety_value=math.inf, 
                       is_obstacle=False, 
                       is_danger=False,
                       safety_value_paths={},
                       path_to_goal=[],
                       sdto_path=[])
            
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

def calculate_direction_target(node, grid_size, disturbance_direction):
    disturbance_target_node = -1
    if(disturbance_direction == 'up'):
        disturbance_target_node = node - grid_size
    elif(disturbance_direction == 'down'):
        disturbance_target_node = node + grid_size
    elif(disturbance_direction == 'left'):
        is_left_edge = node % grid_size == 0
        if not is_left_edge: disturbance_target_node = node - 1
    elif(disturbance_direction == 'right'):
        is_right_edge = node % grid_size == grid_size - 1
        if not is_right_edge: disturbance_target_node = node + 1
    return disturbance_target_node

def graph_random(grid_size, disturbance_direction='right', disturbance_chance_percentage = 25, obstacle_origin_chance = 5, obstacle_origin_max_range = 3, danger_scale=0.15):
    '''Generates a random graph based on the parameters'''
    assert danger_scale >= 0 and danger_scale <= 1
    assert grid_size >= 1

    G = create_unweighted_multidigraph(grid_size,grid_size)
    directions = ['up','down','left','right']
    all_nodes = G.nodes()
    obstacle_nodes = []
    for node in all_nodes:
        if node not in obstacle_nodes:
            is_obstacle_origin = random.randint(1, 101) <= obstacle_origin_chance
            if(is_obstacle_origin):
                obstacle_length = random.randint(1, obstacle_origin_max_range)
                create_obstacle(node, (node+obstacle_length)-1, 1, G)
                obstacle_nodes += [i for i in range(node, node + obstacle_length)]
 
    obstacle_nodes_set = set(obstacle_nodes)
    all_nodes_set = set(all_nodes)
    non_obstacle_nodes = list(all_nodes_set.difference(obstacle_nodes_set))
    danger_count = int(danger_scale * len(non_obstacle_nodes))
    danger_nodes = sorted(non_obstacle_nodes, key=lambda k: random.random())[:danger_count]
    danger_nodes_set = set(danger_nodes)
    for danger_node in danger_nodes:
        create_dangers(danger_node, danger_node, G)

    nodes_with_disturbance = danger_nodes.copy()
    for non_obstacle_node in non_obstacle_nodes:
        if non_obstacle_node in danger_nodes:
            continue

        has_disturbance_blowing = False
        if non_obstacle_node in nodes_with_disturbance:
            has_disturbance_blowing = random.randint(0, 100) <= 80 #disturbance is more likely to be emitted by nodes that already have disturbance leading to them.
        else:
            has_disturbance_blowing = random.randint(0, 100) <= disturbance_chance_percentage

        if has_disturbance_blowing:
            disturbance_target_node = -1
            if(disturbance_direction != 'random'):
                disturbance_target_node = calculate_direction_target(non_obstacle_node, grid_size, disturbance_direction)
            else:
                rnd_disturbance_direction = random.choice(directions)
                disturbance_target_node = calculate_direction_target(non_obstacle_node, grid_size, rnd_disturbance_direction)
            if disturbance_target_node in non_obstacle_nodes:
                create_disturbances_between_nodes(non_obstacle_node, disturbance_target_node, G)
                if disturbance_target_node not in nodes_with_disturbance:
                    nodes_with_disturbance += [disturbance_target_node]

    eligible_nodes = list(set(non_obstacle_nodes).difference(danger_nodes_set))
    return (G, eligible_nodes)

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