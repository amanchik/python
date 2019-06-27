class IndexMinPQ:
    def __init__(self,N):
        self.n = 0
        self.pq = [-1]*N
        self.qp = [-1]*N
        self.keys = {}

    def contains(self, item):
        return self.qp[item] != -1

    def min_key(self):
        return self.keys[self.pq[1]]

    def insert(self,i,val):
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = val
        self.swim(self.n)

    def del_min(self):
        min = self.pq[1]
        self.exch(1,self.n)
        self.n -= 1
        self.sink(1)
        assert min == self.pq[self.n+1]
        self.qp[min] = -1
        del self.keys[min]
        self.pq[self.n+1]= -1
        return min

    def is_empty(self):
        return self.n == 0

    def decrease_key(self,i,val):
        self.keys[i] = val
        self.swim(self.qp[i])

    def swim(self,k):
        while k > 1 and self.greater(k/2,k):
            self.exch(k,k/2)
            k = k/2

    def sink(self,k):
        while 2*k <=  self.n:
            j = 2*k
            if j < self.n and self.greater(j,j+1):
                j += 1
            if not self.greater(k,j):
                break
            self.exch(k,j)
            k = j

    def greater(self,i,j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self,i,j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j