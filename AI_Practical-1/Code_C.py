from collections import deque
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
def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    start_time = time.perf_counter()
    while queue:
        node, path, distance = queue.popleft()
        if node == goal:
            end_time = time.perf_counter()
            return path, distance, (end_time - start_time) * 1000
        if node not in visited:
            visited.add(node)
            for next_node, dist in graph[node]:
                queue.append((next_node, path + [next_node], distance + dist))
def dfs(start, goal):
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
            for next_node, dist in graph[node]:
                stack.append((next_node, path + [next_node], distance + dist))
bfs_path, bfs_distance, bfs_time = bfs("Home", "College")
dfs_path, dfs_distance, dfs_time = dfs("Home", "College")
print("COMPARISON OF BFS AND ITERATIVE DFS")
print("\nBFS")
print("Path      :", " -> ".join(bfs_path))
print("Distance  :", bfs_distance, "km")
print("Time      :", round(bfs_time, 5), "ms")
print("\nIterative DFS")
print("Path      :", " -> ".join(dfs_path))
print("Distance  :", dfs_distance, "km")
print("Time      :", round(dfs_time, 5), "ms")
print("\nConclusion")
if bfs_distance < dfs_distance:
    print("• BFS found the shorter path.")
elif bfs_distance > dfs_distance:
    print("• DFS found the shorter path.")
else:
    print("• Both algorithms found the same distance.")
if bfs_time < dfs_time:
    print("• BFS executed faster.")
else:
    print("• Iterative DFS executed faster.")
