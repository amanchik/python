from graph import Graph
from Queue import Queue
graph = Graph()
n = int(raw_input())
for j in range(n):
    v,w = [int(s) for s in raw_input().split(" ")]
    graph.add_edge(v,w,True)
marked = {}
for x in graph.ad_list:
    marked[x] = False
dist = {}
edge_to = {}
def bfs(s):
    q = Queue()
    for x in graph.ad_list:
        dist[x] = float("inf")
    dist[s] = 0
    marked[s] = True
    q.put(s)
    while not q.empty():
        v = q.get()
        for w in graph.ad_list[v]:
            if not marked[w]:
                edge_to[w] = v
                dist[w] = dist[v] + 1
                marked[w] = True
                q.put(w)
s = int(raw_input())
bfs(s)
print dist
print edge_to
print marked

