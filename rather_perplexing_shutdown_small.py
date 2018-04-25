
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,r,p,s = [int(s) for s in raw_input().split(" ")]
    if n == 1:
        if r == 1 and p == 1 and s == 0:
            print "Case #{}: {}".format(i,'PR')
        elif r == 0 and p == 1 and s == 1:
            print "Case #{}: {}".format(i,'PS')
        elif r == 1 and p == 0 and s == 1:
            print "Case #{}: {}".format(i, 'RS')
        else:
            print "Case #{}: {}".format(i, 'IMPOSSIBLE')
    elif n==2:
        if r == 1 and p == 1 and s == 2:
            print "Case #{}: {}".format(i,'PSRS')
        elif r == 2 and p == 1 and s == 1:
            print "Case #{}: {}".format(i,'PRRS')
        elif r == 1 and p == 2 and s == 1:
            print "Case #{}: {}".format(i, 'PRPS')
        else:
            print "Case #{}: {}".format(i, 'IMPOSSIBLE')
    elif n==3:
        if r == 3 and p == 3 and s == 2:
            print "Case #{}: {}".format(i,'PRPSPRRS')
        elif r == 2 and p == 3 and s == 3:
            print "Case #{}: {}".format(i,'PRPSPSRS')
        elif r == 3 and p == 2 and s == 3:
            print "Case #{}: {}".format(i, 'PRRSPSRS')
        else:
            print "Case #{}: {}".format(i, 'IMPOSSIBLE')

