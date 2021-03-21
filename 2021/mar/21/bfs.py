from collections import defaultdict


class graph:
    def __init__(self):
        self.node = defaultdict(list)

    def add_edge(self, u, v):
        self.node[u].append(v)
    # with stack

    def bfs(self, n, start_node):
        visited = [0 for i in range(n)]
        visited[start_node] = 0
        bfs_trav = []
        temp_stk = []
        temp_stk.append(start_node)
        while len(temp_stk) > 0:
            z = temp_stk.pop(0)
            if visited[z] == 0:
                bfs_trav.append(z)
                visited[z] = 1
                temp_stk.extend(self.node[z])
        print(bfs_trav)


n = int(input("enter number of nodes"))
e = int(input("enter number of edges"))
g1 = graph()
for i in range(e):
    u, v = map(int, input("enter the edges").split(" "))
    g1.add_edge(u, v)
s = int(input("enter the starting vertex"))
g1.bfs(n, s)
