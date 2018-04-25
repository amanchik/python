

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    m = [int(s) for s in raw_input().split(" ")]
    ans  = 0
    for j in range(1,n+1):
        if m[j-1]!=j:
            ans = ans + 1
    print "Case #{}: {}".format(i,str(ans)+".000000")



