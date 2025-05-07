import heapq

class Graph:
    def __init__(self): 
        self.edges = {}  
        self.heuristics = {}  

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((cost, to_node))

    def set_heuristic(self, node, heuristic_value):
        self.heuristics[node] = heuristic_value

    def a_star_search(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (0 + self.heuristics.get(start, 0), 0, start, []))
        visited = {}

        while open_list:
            f, g, current, path = heapq.heappop(open_list)
            path = path + [current]

            if current == goal:
                return path, g  

            if current in visited and visited[current] <= g:
                continue
            visited[current] = g

            for cost, neighbor in self.edges.get(current, []):
                new_g = g + cost
                new_f = new_g + self.heuristics.get(neighbor, 0)  # Default heuristic to 0 instead of inf
                heapq.heappush(open_list, (new_f, new_g, neighbor, path))

        return None, float('inf')  

graph = Graph()

num_edges = int(input("Enter number of edges: "))
print("Enter edges in the format (From To Cost):")
for _ in range(num_edges):
    from_node, to_node, cost = input().split()
    graph.add_edge(from_node, to_node, int(cost))

num_nodes = int(input("Enter number of nodes: "))
print("Enter heuristic values in the format (Node Heuristic):")
for _ in range(num_nodes):
    node, heuristic = input().split()
    graph.set_heuristic(node, int(heuristic))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = graph.a_star_search(start, goal)
if path:
    print(f"Optimal Path: {' -> '.join(path)}")
    print(f"Total Cost: {cost}")
else:
    print("No path found!")
