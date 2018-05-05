

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    p,k,l = [int(s) for s in raw_input().split(" ")]
    f = [int(s) for s in raw_input().split(" ")]
    f.sort()
    f = f[::-1]
    tmp = k
    current = 1
    ans = 0
    for x in f:
        ans += x*current
        tmp -= 1
        if tmp == 0:
            tmp = k
            current += 1

    print "Case #{}: {}".format(i,ans)



