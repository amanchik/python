import sys
import math
pi = 4*math.atan(1)
#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    a,b = [int(s) for s in raw_input().split(" ")]
   # print a,b
    #sys.stdout.flush()
    p =  [float(s) for s in raw_input().split(" ")]
    minp = b+2
    pr = 1
    for r in range(a+1):
        if r>0:
            pr = pr * p[r-1]
        ans = (a+2*b-2*r+2)*(1-pr) + (a+b+1-2*r)*pr
        if ans<minp:
            minp = ans
    st = "{0:.15f}".format(minp)
    print "Case #{}: {}".format(i,st)



