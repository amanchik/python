

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    m = [int(s) for s in raw_input().split(" ")]
    n = m[0]
    m = m[1:]
    J = sum(m)
    total = 2*J
    sm = reversed(sorted(m))
    for x in sm:
        if x*n <= total or n==1:
            break
        else:
            n = n - 1
            total = total-x
    eq = total*1.0/n
   # print eq

    ans = [0.0 if x>eq else (eq-x)*100.0/J for x in m]
    ans = ["{0:.15f}".format(x) for x in ans]

    print "Case #{}: {}".format(i,' '.join(ans))



