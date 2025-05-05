from dataSet import graph
def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, _ in reversed(graph.get(node, [])):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None
path =dfs('A','G')
print("THE path using DFS is ",path)