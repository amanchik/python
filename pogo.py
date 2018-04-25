

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    x,y = [int(s) for s in raw_input().split(" ")]
    ans = ''
    if x>0:
        ans += ('WE'*x)
    else:
        ans += ('EW'*(-1*x))
    if y>0:
        ans += ('SN'*y)
    else:
        ans += ('NS'*(-1*y))

    print "Case #{}: {}".format(i,ans)



