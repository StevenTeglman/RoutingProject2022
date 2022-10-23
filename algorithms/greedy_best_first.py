from timeit import default_timer as timer
from util import graph as gr

# Adapted from Pseudo code from Wikiepedia: https://en.wikipedia.org/wiki/Best-first_search
def algorithm(graph, start, end):
    # Used to sort the queue
    def get_heuristic(node):
        return node.get('heuristic')
    
    # For statistics
    operations = 0
    start_time = timer()
    
    # Function variables
    visited = []
    queue = []
    path = []
    heuristics = gr.get_all_manhattan(graph)
    visited.append(start)
    queue.append({"Node": start,
                  "heuristic": heuristics[start][end]})
    
    while queue:
        queue.sort(key=get_heuristic)
        current_node = queue.pop(0)
        path.append(current_node["Node"])
        for neighbor in graph[current_node["Node"]]:
            operations += 1
            if neighbor not in visited:
                if neighbor == end:
                    end_time = timer()
                    stats = {"Operations": operations,
                             "Time_Secs": end_time - start_time}
                    return path, stats
                else:
                    visited.append(neighbor)
                    queue.append({"Node": neighbor,
                                  "heuristic": heuristics[neighbor][end]})
    return False
    