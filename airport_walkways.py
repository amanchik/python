

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    x,sp,r,t,n = [int(s) for s in raw_input().split(" ")]
    bew = []
    wd = 0

    for j in range(n):
        b,e,w = [int(s) for s in raw_input().split(" ")]
        bew.append((b,e,w))
        wd += (e - b)

    bew.sort(key=lambda x: x[2])
    ans = 0
    rwd = x - wd
    if r * t >= rwd:
        ans += 1.0 * rwd / r
        t = t - 1.0 *rwd/r
    else:
        ans += (1.0 * (rwd - t * r) / sp)
        ans += t
        t = 0

    for (b,e,w) in bew:
        if (w+r)*t>=e-b:
            ans += 1.0*(e-b)/(w+r)
            t = t - 1.0*(e-b)/(w+r)
        elif t>0:
            ans += 1.0*(e-b-t*(w+r))/(w+sp)
            ans += t
            t = 0
        else:
            ans += 1.0*(e-b)/(w+sp)


    st = "{0:.15f}".format(ans)
    print "Case #{}: {}".format(i,st)



