import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        for edge_cost, neighbor in graph[node]:
            new_cost = cost + edge_cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return dist

graph = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(2, 'C'), (6, 'D')],
    'C': [(3, 'D')],
    'D': []
}

print("Distances:", dijkstra(graph, 'A'))
