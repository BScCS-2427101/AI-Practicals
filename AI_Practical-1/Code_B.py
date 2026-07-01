graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []
stack = []

start = 'A'

stack.append(start)

print("DFS Traversal:")

while stack:
    node = stack.pop()

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in reversed(graph[node]):
            stack.append(neighbour)