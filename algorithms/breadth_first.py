def algorithm(graph, start, end, path=[], frontier=[], visited=[]):
    visited.append(start)
    if not frontier and start not in path:
        path += [start]
    if start == end:
        return path
    
    if start not in graph.nodes():
        return None
    
    for node in graph[start]:
        if node not in visited:
            new_path = path + [node]
            frontier += [new_path]
    if path in frontier:
        frontier.remove(path)

    return algorithm(graph, frontier[0][-1], end, frontier[0], frontier, visited)