from math import inf
from timeit import default_timer as timer

def algorithm(graph, start, end):
    # For statistics
    operations = 0
    start_time = timer()
    
    unvisited = list(graph)
    shortest = {}
    previous = {start: -1}
    for v in unvisited:
        shortest[v] = inf
    shortest[start] = 0
    while len(unvisited):
        operations += 1
        curr_min = None
        for v in unvisited:
            if curr_min == None or shortest[v] < shortest[curr_min]: 
                curr_min = v
        connections = graph[curr_min]

        for connection in connections:
            edgeval = shortest[curr_min] + graph[curr_min][connection]['weight'] #assume each edge weight is equal (= 1)
            if edgeval < shortest[connection]:
                shortest[connection] = edgeval
                previous[connection] = curr_min
        unvisited.remove(curr_min)
    end_time = timer()
    stats = {"Operations": operations,
             "Time_Secs": end_time - start_time}

    return backtrack(start, end, previous), stats


def backtrack(start, end, prev): 
    path = [end]
    tmp = end
    while tmp != -1:
        tmp = prev[tmp]
        if tmp > -1:
            path.append(tmp)
    return path[::-1]
