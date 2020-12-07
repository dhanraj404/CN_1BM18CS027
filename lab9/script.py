import sys 
   
class Network(): 
   
    def __init__(self, nodes): 
        self.V = nodes 
        self.graph = [[0 for column in range(nodes)]  
                    for row in range(nodes)] 
   
    def printTable(self, dist,src,path): 
        print("Shortest Path Table for Scource -> {}".format(src))  
        print("Destination \t Distance \t path")
        for node in range(self.V): 
            print("{0}\t\t{1}\t\t{2}".format(node, dist[node],path[node]))

    def minDistance(self, dist, sptSet): 
        min = sys.maxsize 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 
    def dijkstra(self, src): 
   
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
        path={}
        for _ in range(self.V):
            path[_]=[]
        for _ in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
                    if u == src:
                        path[v].append(v)
                    else:
                        path[v].append(u)
                        path[v].append(v)
   
        self.printTable(dist,src,path) 
        
   
# Driver program 
v = int(input("Enter Number of vertices: "))

G = Network(v) 
g = []
print("Enter the Matrix:")
for _ in range(4):
    gg = list(map(int, input().split()))
    g.append(gg)
G.graph = g
   
for v in range(G.V):
    G.dijkstra(v)