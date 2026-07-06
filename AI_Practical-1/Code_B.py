import time
graph = {
    "Home": [("Bus Stop", 2), ("Hospital", 3), ("Park", 4)],
    "Bus Stop": [("Railway", 2)],
    "Hospital": [("Temple", 2)],
    "Park": [("Mall", 2)],
    "Railway": [("College", 3)],
    "Temple": [("College", 2)],
    "Mall": [("College", 4)],
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
            for neighbour, dist in reversed(graph[node]):
                stack.append((neighbour,
                              path + [neighbour],
                              distance + dist))
    return None
path, distance, t = iterative_dfs("Home", "College")
print("Iterative DFS Result")
print("Path :", " -> ".join(path))
print("Distance :", distance, "km")
print("Time :", round(t, 5), "ms")
