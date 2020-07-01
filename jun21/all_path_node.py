from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            fnode.extend(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


global fnode
fnode = []
n = int(input())
k = {}
k1 = []
im_ng = []
for i in range(n):
    z = int(input())
    k[z] = i
    k1.append(z)
m1 = max(k1)
# Create a graph given in the above diagram
g = Graph(m1+1)
ed = int(input())
for i in range(ed):
    a, b = map(int, input().split())
    g.addEdge(a, b)

s, d = map(int, input().split())
g.printAllPaths(s, d)
# This code is contributed by Neelam Yadav
for i in k1:
    if d in g.graph[i]:
        im_ng.append(i)
fnode = list(set(fnode))
fnode.sort()
for i in im_ng:
    if i in fnode:
        print(i, end=" ")
