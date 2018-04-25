

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,l,h = [int(s) for s in raw_input().split(" ")]
    f = [int(s) for s in raw_input().split(" ")]
    ans = -1
    for k in range(l,h+1):
        possible = True
        for x in f:
            if x%k != 0 and k%x != 0 :
                possible = False
                break
        if possible:
            ans = k
            break
    if ans == -1:
        print "Case #{}: {}".format(i,"NO")
    else:
        print "Case #{}: {}".format(i,ans)




