from dataSet import graph
import heapq
def ucs(start, goal):# prQueue:
    queue = [(0, start, [start])]
    visited = {}

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost

        for neighbor, weight in graph[node]:
            heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')


path, total_cost = ucs('A', 'G')
print("UCS Path:", " → ".join(path))
print("Total Cost:", total_cost)
