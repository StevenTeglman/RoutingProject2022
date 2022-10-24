from timeit import default_timer as timer

def algorithm(graph, start, end, path=[]):
    # For statistics
    start_time = timer()    
    
    path = path + [start]
    if start == end:
        end_time = timer()
        stats = {"Time_Secs": end_time - start_time}
        return path, stats
    
    if start not in graph.nodes():
        return None
    
    for node in graph[start]:
        if node not in path:
            newpath = algorithm(graph, node, end, path)
            if newpath: return newpath