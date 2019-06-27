def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
t = int(raw_input()) # read a line with a single integer
def get_range(x,y):
    below = (10*y)/(11*x)
    if (10*y)%(11*x) != 0 :
        below += 1
    above = (10*y)/(9*x)
    if below <= above:
        return (below,above)
    else:
        return (0,0)
def intersect(x,y):
    if x[0] <= y[1] and y[0] <= x[1]:
        return  True
    return False
def not_zero(a):
    return a[1] != 0
def get_count(a,b):
    if len(a) != len(b):
        return 0
    ans = 0
    for j in range(len(a)):
        if not_zero(a[j]) and not_zero(b[j]) and intersect(a[j],b[j]):
            ans += 1
    return  ans


for i in xrange(1, t + 1):
    n,p =  [int(s) for s in raw_input().split(" ")]
    r = [int(s) for s in raw_input().split(" ")]
    q = []
    for j in range(n):
        q.append([int(s) for s in raw_input().split(" ")])
    mq = []
    for j in range(n):
        x = r[j]
        mq.append([get_range(x,y) for y in q[j]])
   # print mq
    if n == 1:
        ans = 0
        for x in mq[0]:
            if  not (x[0] == 0 and x[1] == 0):
                ans += 1
    else:
        ans = 0
        for x in permutations(mq[1],p):
            tmp = get_count(mq[0],x)
            if tmp > ans:
                ans = tmp
                if ans == p:
                    break
    print "Case #{}: {}".format(i, ans)