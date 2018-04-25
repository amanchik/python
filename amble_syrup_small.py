import math
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


pi = 4*math.atan(1)
#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,k = [int(s) for s in raw_input().split(" ")]
    rs = []
    hs = []
    index = range(0,n)
    for j in range(n):
        r,h = [int(s) for s in raw_input().split(" ")]
        rs.append(r)
        hs.append(h)
    rhs= zip(index,rs,hs)
    drhs = combinations(rhs,k)
    max_ans = 0
    for ps in drhs:
        ps = list(ps)
        ps.sort(key=lambda x: x[1])
        ans = sum([2*a[1]*a[2] for a in ps]) + ps[-1][1]* ps[-1][1]
        if ans>max_ans:
            max_ans = ans
    max_ans = max_ans*pi
    print n,k
    st = "{0:.15f}".format(max_ans)
    print "Case #{}: {}".format(i,st)

