from collections import defaultdict


class graph:
    def __init__(self):
        self.node = defaultdict(list)

    def add_edge(self, u, v):
        self.node[u].append(v)
    # with stack

    def bfs_level(self, n, start_node):
        visited = [0 for i in range(n)]
        visited[start_node] = 0
        bfs_trav = []
        l0 = []
        l1 = []
        visited[start_node] = 1
        l0.append(start_node)
        bfs_trav.append(l0)
        l1.append(self.node[start_node])
        l0 = l1
        l1 = []
        while len(l0) > 0:
            az = []
            for i in l0:
                if visited[i] == 1:
                    l1.append(self.node[i])
                    az.append(i)
            bfs_trav.append(az)
            l0 = l1
            l1 = []
        print(bfs_trav)


n = int(input("enter number of nodes"))
e = int(input("enter number of edges"))
g1 = graph()
for i in range(e):
    u, v = map(int, input("enter the edges").split(" "))
    g1.add_edge(u, v)
s = int(input("enter the starting vertex"))
g1.bfs_level(n, s)
