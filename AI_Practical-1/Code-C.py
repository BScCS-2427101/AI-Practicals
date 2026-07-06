from collections import deque
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
def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    s = time.perf_counter()
    while queue:
        node, path, distance = queue.popleft()
        if node == goal:
            e = time.perf_counter()
            return path, distance, (e - s) * 1000
        if node not in visited:
            visited.add(node)
            for neighbour, dist in graph[node]:
                queue.append((neighbour,
                              path + [neighbour],
                              distance + dist))
def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    s = time.perf_counter()
    while stack:
        node, path, distance = stack.pop()
        if node == goal:
            e = time.perf_counter()
            return path, distance, (e - s) * 1000
        if node not in visited:
            visited.add(node)
            for neighbour, dist in reversed(graph[node]):
                stack.append((neighbour,
                              path + [neighbour],
                              distance + dist))
bfs_path, bfs_distance, bfs_time = bfs("Home", "College")
dfs_path, dfs_distance, dfs_time = dfs("Home", "College")
print("COMPARISON")
print("\nBFS")
print("Path :", " -> ".join(bfs_path))
print("Distance :", bfs_distance, "km")
print("Time :", round(bfs_time, 5), "ms")
print("\nIterative DFS")
print("Path :", " -> ".join(dfs_path))
print("Distance :", dfs_distance, "km")
print("Time :", round(dfs_time, 5), "ms")
print("\nConclusion")
if bfs_distance < dfs_distance:
    print("BFS found a shorter path.")
elif bfs_distance > dfs_distance:
    print("DFS found a shorter path.")
else:
    print("Both algorithms found the same distance.")
if bfs_time < dfs_time:
    print("BFS executed faster.")
else:
    print("Iterative DFS executed faster.")
