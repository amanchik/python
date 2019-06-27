from index_min_pq import IndexMinPQ
from weighted_graph import WeighedGraph
wg = WeighedGraph()
N = int(raw_input())
n = int(raw_input())
for j in range(n):
    s = raw_input().split(" ")
    wg.add_edge(int(s[0]),int(s[1]),float(s[2]),False)
class Dijkstra:
    def __init__(self,digraph,source,N):
        self.distTo = [float('inf')]*N
        self.edgeTo = {}
        self.distTo[source] = 0.0
        self.pq = IndexMinPQ(N)
        self.pq.insert(source,self.distTo[source])

        while not self.pq.is_empty():
            v = self.pq.del_min()
            for e in digraph.ad_list[v]:
                self.relax(e)

    def relax(self,e):
        v = e[0]
        w = e[1]
        weight = e[2]
        if self.distTo[w] > self.distTo[v] + weight:
            self.distTo[w] = self.distTo[v] + weight
            self.edgeTo[w] = e
            if self.pq.contains(w):
                self.pq.decrease_key(w,self.distTo[w])
            else:
                self.pq.insert(w,self.distTo[w])

    def has_path_to(self,v):
        return self.distTo[v] < float('inf')


    def path_to(self,v):
        ans = []
        while v in self.edgeTo:
            ans.append(self.edgeTo[v])
            v = self.edgeTo[v][0]
        return ans


dsp = Dijkstra(wg,0,N)
print  dsp.path_to(6)


