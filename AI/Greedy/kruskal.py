def kruskal_mst(edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root

    edges.sort()
    total_cost = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += cost

    return total_cost

edges = [
    (1, 0, 1),
    (4, 0, 2),
    (2, 1, 2),
    (6, 1, 3),
    (3, 2, 3)
]
n = 4
print("Total Cost:", kruskal_mst(edges, n))
