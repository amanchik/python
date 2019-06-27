from min_pq import MinPQ
class CubeSum(object):
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.sum = i**3 + j**3

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __lt__(self, other):
        return self.sum < other.sum

    def __gt__(self, other):
        return self.sum > other.sum

    def __str__(self):
        return str(self.sum) + " = " + str(self.i) + "^3" + " + " + str(self.j) + "^3"

mpq = MinPQ()
for  i in range(13):
    mpq.insert(CubeSum(i,i))


while not mpq.is_empty():
    s = mpq.del_min()
    print s
    if s.j < 12 :
        mpq.insert(CubeSum(s.i,s.j+1))
