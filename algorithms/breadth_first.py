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
            frontier.append(new_path)
    if path in frontier:
        frontier.remove(path)

    for i in frontier:
        if i[-1] in visited:
            frontier.remove(i)

    return algorithm(graph, frontier[0][-1], end, frontier[0], frontier, visited)


def non_recursive_algorithm(graph, start, goal):
    visited = []
    queue = [[start]]

    while queue:
        current_path = queue.pop(0)
        exploring = current_path[-1]

        if exploring == goal:
            return current_path

        for node in graph[exploring]:
            if node not in visited:
                queue.append(current_path + [node])

        visited.append(exploring)

        for path in queue:
            if path[-1] in visited:
                queue.remove(path)
