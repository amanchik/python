def hcf(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a%b == 0:
        return b
    elif b%a == 0:
        return a
    elif a>b:
        return hcf(b,a%b)
    else:
        return hcf(a,b%a)

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,m = [int(s) for s in raw_input().split(" ")]
    sd = []
    cd = []
    for j in range(n):
        sd.append(raw_input())
    for j in range(m):
        cd.append(raw_input())
    ans = 0
    for x in cd:
        parts = x.split('/')
        while len(parts) > 1:
         #   print sd
            if '/'.join(parts) not in sd:
                sd.append('/'.join(parts))
                ans = ans + 1
            parts.pop()




    print "Case #{}: {}".format(i,ans)






