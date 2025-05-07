import heapq

def prims_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            total_cost += cost
            for nei_cost, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (nei_cost, nei))

    return total_cost

graph = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(1, 'A'), (2, 'C'), (6, 'D')],
    'C': [(4, 'A'), (2, 'B'), (3, 'D')],
    'D': [(6, 'B'), (3, 'C')]
}

print("Total Cost:", prims_mst(graph, 'A'))
