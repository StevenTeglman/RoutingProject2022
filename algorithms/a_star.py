import util.graph as gr
from math import inf
from timeit import default_timer as timer
import networkx as nx

def algorithm2(graph, start, end):
    # For statistics
    start_time = timer()
    
    # Add the start node in a tuple with the format ([PATH], TOTAL_COST)
    # to the frontier.
    frontier = [([start], 0)]
    while frontier:
        frontier_node_to_expand = frontier.pop(0)
        current_path = frontier_node_to_expand[0]
        current_path_cost = len(current_path) - 1
        path_last_node = current_path[-1]
        
        
        # If expanded node is goal, return path
        if end == path_last_node:
            end_time = timer()
            stats = {"Time_Secs": end_time - start_time}
            return current_path, stats
        
        # Collect all of the neighbors not connected by disturbance edges
        neighbors = []
        for k, v in graph[path_last_node].items():
            for k2, v2 in v.items():
                if not v2["is_disturbance"]:
                    if not graph.nodes[k]["is_danger"] and not graph.nodes[k]["is_obstacle"]:
                        neighbors.append(k)
                        break
        
        print(f"Current Path: {current_path}")
        # Add each neighbor to the frontier, with their total cost
        for neighbor in neighbors:
            graph.nodes[neighbor]['color'] = 'orange'
            new_path = []
            new_path = current_path.copy()
            new_path.append(neighbor)
            new_frontier_cost = len(new_path)-1
            new_frontier_heuristics = nx.shortest_path_length(graph, source=neighbor, target=end)
            new_frontier_total_cost = new_frontier_cost + new_frontier_heuristics
            new_frontier_path = (new_path, new_frontier_total_cost)
            frontier.append(new_frontier_path)
        
        frontier.sort(key=lambda x:x[1])
        print(frontier)
            
            
        # Sort frontier with lowest cost first    
    
    # No path was found...
    print("No Path Found")
    return False, False

def algorithm(graph, start, end):
    # For statistics
    start_time = timer()
    key = 0
    unvisited = list(graph)
    total_cost = {}
    cost_plus_hueristics = {}
    previous = {start: -1}
    # hu_start_time = timer()
    # hueristics = gr.get_all_manhattan(graph)
    # hu_end_time = timer()
    # hu_elapsed_time = hu_end_time - hu_start_time

    for v in unvisited:
        cost_plus_hueristics[v] = inf
        total_cost[v] = inf
        
    cost_plus_hueristics[start] = 0
    total_cost[start] = 0
    while len(unvisited):
        # print(total_cost)
        current_node = None
        for v in unvisited:
            if current_node == None or cost_plus_hueristics[v] < cost_plus_hueristics[current_node]: 
                current_node = v
        neighbours = graph[current_node]
        
        for neighbour in neighbours:
            graph.nodes[neighbour]['color'] = 'orange'
            edge_cost = total_cost[current_node] + graph[current_node][neighbour][key]['weight'] #assume each edge weight is equal (= 1)
            # total_edge_cost = edge_cost + hueristics[neighbour][end]
            total_edge_cost = edge_cost + nx.shortest_path_length(graph, source=current_node, target= neighbour)
            # print("Node: " + str(neighbour))
            # print("total edge cost: " + str(total_edge_cost))
            # print("edge_cost: " + str(edge_cost) + "\n")
            if edge_cost < total_cost[neighbour]:
                total_cost[neighbour] = edge_cost
                cost_plus_hueristics[neighbour] = total_edge_cost
                previous[neighbour] = current_node
        unvisited.remove(current_node)
    end_time = timer()
    stats = {"Time_Secs": end_time - start_time}
    return backtrack(start, end, previous), stats                



def backtrack(start, end, prev): 
    path = [end]
    tmp = end
    while tmp != -1:
        tmp = prev[tmp]
        if tmp > -1:
            path.append(tmp)
    return path[::-1]
