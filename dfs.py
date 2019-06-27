from graph import Graph

graph = Graph()
n = int(raw_input())
for j in range(n):
    v,w = [int(s) for s in raw_input().split(" ")]
    graph.add_edge(v,w,True)
marked = {}
for x in graph.ad_list:
    marked[x] = False
def dfs(s):
    marked[s] = True
    for x in graph.ad_list[s]:
        if not marked[x]:
            dfs(x)
s = int(raw_input())
dfs(s)
print marked