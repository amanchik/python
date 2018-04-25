import math
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
    hrs = [(2*r*h,2*r*h+r*r,r,h,j) for (j,r,h) in rhs]
    if k>1:
        hrs.sort(key=lambda x: x[1])
        hrs=hrs[::-1]
        chrs = [x for x in hrs]
        chrs.sort(key=lambda x: x[0])
        chrs = chrs[::-1]
        max_ans = 0
        for xx in hrs:
            ans = xx[1]
            fhrs = [x  for x in chrs if x[2]<=xx[2] and x[4]!=xx[4]]
            if len(fhrs)<k-1:
                continue
            ans += sum([x[0] for x in fhrs[0:k-1]])
            if ans>max_ans:
                max_ans = ans




        ans = max_ans * pi
        st = "{0:.15f}".format(ans)
        print "Case #{}: {}".format(i,st)
    else:
        hrs.sort(key=lambda x: x[1])
       # print hrs
        ans = hrs[-1][1]
        ans = ans * pi
        st = "{0:.15f}".format(ans)
        print "Case #{}: {}".format(i,st)

