import sys
def distance(i,j):
    global matrix
    dist = 0
    while i<j:
        dist += matrix[i-1][i]
        i += 1
    return dist
def get_min_time(i):
    global matrix,es,n,cache
    if i == n :
        cache[i] = 0.0
        return 0.0
    if cache[i] != -1:
        return cache[i]
    min_time = 9999999999999999
    for j in reversed(range(i+1,n+1)):
        if distance(i,j) <= es[i-1][0]:
            one_time = (1.0*distance(i,j)/es[i-1][1]) + get_min_time(j)
            if one_time < min_time:
                min_time = one_time
    cache[i] = min_time
    return min_time





t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,q = [int(s) for s in raw_input().split(" ")]
    es = []
    for j in range(n):
        e,s = [int(s) for s in raw_input().split(" ")]
        es.append((e,s))
    matrix = []
    for _ in range(n):
        mx = [int(s) for s in raw_input().split(" ")]
        matrix.append(mx)
    destinations = []
    for _ in range(q):
        u,v = [int(s) for s in raw_input().split(" ")]
        destinations.append((u,v))
  #  print n,q
  #  print es

    cache = [-1 for j in range(n+1)]

    st = "{0:.15f}".format(get_min_time(1))
    print "Case #{}: {}".format(i,st)
   # print cache
    sys.stdout.flush()




