
def algorithm(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    
    if start not in graph.nodes():
        return None
    
    for node in graph[start]:
        if node not in path:
            newpath = algorithm(graph, node, end, path)
            if newpath: return newpath