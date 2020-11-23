class Network:
    def __init__(self,n):
        self.matrix=[]
        self.n=n 
        
    def addlink(self, u, v, w):  
        self.matrix.append((u, v, w)) 
        
    def printtable(self, dist,src, out):
        print("Router Table entries for router {}".format(chr(ord('A')+src)))
        print("{0}\t{1}\t{2}".format("Dest", "Hop", "Out"))  
        for i in range(self.n):  
            print("{0}\t{1}\t{2}".format(chr(ord('A')+i), dist[i], out))  
    #Bellman-Ford
    def solve(self, src):          
        dist = [99] * self.n 
        dist[src] = 0
        flag = True
        out = ""
        for _ in range(self.n - 1):  
            for u, v, w in self.matrix:  
                if dist[u] != 99 and dist[u] + w < dist[v]: 
                        if flag:
                            out = chr(ord('A')+dist[u]+w)
                            flag = False
                        dist[v] = dist[u] + w  
        self.printtable(dist,src, out)  


if __name__ == "__main__":
    matrix=[]
    n=int(input("Enter No. of Routers : "))
    print("Enter the Router dist Matrix :")
    for i in range(n):
        row=list(map(int,input().split(" ")))
        matrix.append(row)
    g=Network(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                g.addlink(i,j,1)
    
    for i in range(n):
        g.solve(i)
    