import time
graph = {
    "Home": [("Bus Stop", 2), ("Hospital", 3), ("Park", 2)],
    "Bus Stop": [("Railway", 2)],
    "Railway": [("Library", 1)],
    "Library": [("College", 2)],
    "Hospital": [("Temple", 2)],
    "Temple": [("Garden", 2)],
    "Garden": [("College", 2)],
    "Park": [("Mall", 2)],
    "Mall": [("Cinema", 2)],
    "Cinema": [("Stadium", 2)],
    "Stadium": [("College", 3)],
    "College": []
}
def iterative_dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    start_time = time.perf_counter()
    while stack:
        node, path, distance = stack.pop()
        if node == goal:
            end_time = time.perf_counter()
            return path, distance, (end_time - start_time) * 1000
        if node not in visited:
            visited.add(node)
            for neighbour, dist in graph[node]:
                stack.append((neighbour,
                              path + [neighbour],
                              distance + dist))
    return None
path, distance, t = iterative_dfs("Home", "College")
print("===== Iterative DFS Result =====")
print("Path :", " -> ".join(path))
print("Distance :", distance, "km")
print("Time :", round(t, 5), "ms")
