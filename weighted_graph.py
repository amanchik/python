class WeighedGraph:
    def __init__(self):
        self.ad_list = {}

    def add_edge(self,v,w,weight,undirected):
        if v not in self.ad_list:
            self.ad_list[v] = []
        self.ad_list[v].append((v,w,weight))
        if undirected:
            if w not in self.ad_list:
                self.ad_list[w] = []
            self.ad_list[w].append((w,v,weight))