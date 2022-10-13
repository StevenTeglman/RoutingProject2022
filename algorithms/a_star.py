import util.graph as gr
from math import inf

def algorithm(graph, start, end):
    unvisited = list(graph)
    total_cost = {}
    cost_plus_hueristics = {}
    previous = {start: -1}
    hueristics = gr.get_all_manhattan(graph)
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
            edge_cost = total_cost[current_node] + graph[current_node][neighbour]['weight'] #assume each edge weight is equal (= 1)
            total_edge_cost = edge_cost + hueristics[neighbour][end]
            print("Node: " + str(neighbour))
            print("total edge cost: " + str(total_edge_cost))
            print("edge_cost: " + str(edge_cost) + "\n")
            if edge_cost < total_cost[neighbour]:
                total_cost[neighbour] = edge_cost
                cost_plus_hueristics[neighbour] = total_edge_cost
                previous[neighbour] = current_node
        unvisited.remove(current_node)
    return backtrack(start, end, previous)


def backtrack(start, end, prev): 
    path = [end]
    tmp = end
    while tmp != -1:
        tmp = prev[tmp]
        if tmp > -1:
            path.append(tmp)
    return path[::-1]
