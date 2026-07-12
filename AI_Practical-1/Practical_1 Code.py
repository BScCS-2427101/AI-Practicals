from collections import deque
import time
graph = graph = {
    "Home": [
        ("Bus Stop", 2, "Left"),
        ("Hospital", 3, "Straight"),
        ("Park", 2, "Right")
    ],
    "Bus Stop": [("Railway", 2, "Straight")],
    "Railway": [("Library", 1, "Straight")],
    "Library": [("College", 2, "Straight")],
    "Hospital": [("Temple", 2, "Straight")],
    "Temple": [("Garden", 2, "Straight")],
    "Garden": [("College", 2, "Straight")],
    "Park": [("Mall", 2, "Straight")],
    "Mall": [("Cinema", 2, "Straight")],
    "Cinema": [("Stadium", 2, "Straight")],
    "Stadium": [("College", 3, "Straight")],
    "College": []
}
def bfs(start, goal):
    queue = deque([(start, [start], 0, [])])
    visited = set()
    start_time = time.perf_counter()
    while queue:
        node, path, distance, details = queue.popleft()
        if node == goal:
            end_time = time.perf_counter()
            return path, distance, details, (end_time - start_time) * 1000
        if node not in visited:
            visited.add(node)
            for next_node, dist, direction in graph[node]:
                queue.append((
                    next_node,
                    path + [next_node],
                    distance + dist,
                    details + [(node, next_node, dist, direction)]
                ))
def dfs(start, goal):
    stack = [(start, [start], 0, [])]
    visited = set()
    start_time = time.perf_counter()
    while stack:
        node, path, distance, details = stack.pop()
        if node == goal:
            end_time = time.perf_counter()
            return path, distance, details, (end_time - start_time) * 1000
        if node not in visited:
            visited.add(node)
            for next_node, dist, direction in graph[node]:
                stack.append((
                    next_node,
                    path + [next_node],
                    distance + dist,
                    details + [(node, next_node, dist, direction)]
                ))
bfs_path, bfs_distance, bfs_details, bfs_time = bfs("Home", "College")
dfs_path, dfs_distance, dfs_details, dfs_time = dfs("Home", "College")
print("COMPARISON OF BFS AND ITERATIVE DFS")
print("\nBreadth First Search (BFS)")
print("Path :", " -> ".join(bfs_path))
print("Route:")
for source, destination, dist, direction in bfs_details:
    print(source, "--", direction, "--", dist, "km -->", destination)
print("Total Distance :", bfs_distance, "km")
print("Execution Time :", round(bfs_time, 5), "ms")
print("\nIterative Depth First Search (DFS)")
print("Path :", " -> ".join(dfs_path))
print("Route:")
for source, destination, dist, direction in dfs_details:
    print(source, "--", direction, "--", dist, "km -->", destination)
print("Total Distance :", dfs_distance, "km")
print("Execution Time :", round(dfs_time, 5), "ms")
if bfs_distance < dfs_distance:
    print("BFS found the shorter path and travelled less distance.")
elif dfs_distance < bfs_distance:
    print("DFS found the shorter path.")
else:
    print("Both algorithms travelled the same distance.")
if bfs_time < dfs_time:
    print("BFS executed faster.")
else:
    print("Iterative DFS executed faster.")
