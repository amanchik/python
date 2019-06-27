class MinPQ:
    def __init__(self):
        self.pq = [-1]

    def insert(self,v):
        self.pq.append(v)
        self.swim(len(self.pq)-1)

    def swim(self,k):
        while k>1 and self.greater(k/2,k):
            self.exch(k,k/2)
            k = k/2

    def sink(self,k):
        while 2*k <= len(self.pq)-1:
            j = 2*k
            if j < len(self.pq)-1 and self.greater(j,j+1): j += 1
            if not self.greater(k,j): break
            self.exch(k,j)
            k = j

    def is_empty(self):
        return len(self.pq) == 1

    def del_min(self):
        min = self.pq[1]
        self.pq[1] = self.pq[-1]
        self.pq.pop()
        self.sink(1)
        return min

    def greater(self,i,j):
        return self.pq[i] > self.pq[j]

    def exch(self,i,j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap