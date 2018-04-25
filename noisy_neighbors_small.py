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

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    r,c,n = [int(s) for s in raw_input().split(" ")]

    zeros = 0
    for j in range(r):
        if j%2 == 0 and c%2==1:
            zeros += (c/2)+1
        else:
            zeros += (c/2)
    if n<=zeros:
        print "Case #{}: {}".format(i, 0)
    else:

        product = range(r*c)
        possibles = combinations(product,n)
        min_ans = 10000
        for poss in possibles:
            occupied = [[False for j in range(c)] for k in range(r)]
            for j in range(r):
                for k in range(c):
                    if j*c + k in poss:
                        occupied[j][k] = True
            ans = 0
            for j in range(r):
                for k in range(c):
                    if occupied[j][k]:
                        if j > 0 and occupied[j - 1][k]:
                            ans += 1
                        if j + 1 < r and occupied[j + 1][k]:
                            ans += 1
                        if k > 0 and occupied[j][k - 1]:
                            ans += 1
                        if k + 1 < c and occupied[j][k + 1]:
                            ans += 1
            if ans < min_ans:
                min_ans = ans
                comb = occupied
      #  print comb
        print "Case #{}: {}".format(i,min_ans/2)



