g = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3, 1]
}

def dfs(g, s):
    vis[s] = 1
    print(s)
    for c in g[s]:
        if not vis[c]:
            dfs(g, c)

def bfs(g,s):
    q=[s]
    vis[s]
    while q:
        cur=q.pop(0)
        print(cur)
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)


vis = [0] * 5 
dfs(g, 0)
print("The bfs is")
bfs(g,0)