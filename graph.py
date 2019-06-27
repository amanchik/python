class Graph:
    def __init__(self):
        self.ad_list = {}

    def add_edge(self,v,w,undirected):
        if v not in self.ad_list:
            self.ad_list[v] = []
        self.ad_list[v].append(w)
        if undirected:
            if w not in self.ad_list:
                self.ad_list[w] = []
            self.ad_list[w].append(v)