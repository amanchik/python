

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    v1 = [int(s) for s in raw_input().split(" ")]
    v2 = [int(s) for s in raw_input().split(" ")]
    v1.sort()
    v2.sort()
    v2 = v2[::-1]
    ans = 0
    for j in range(n):
        ans += (v1[j]*v2[j])

    print "Case #{}: {}".format(i,ans)



