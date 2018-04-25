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
    n = int(raw_input())
    sd = []
    cd = []
    for j in range(n):
        a,b =[int(s) for s in raw_input().split(" ")]
        sd.append(a)
        cd.append(b)
    ans = 0
    for j in range(n):
        for k in range(j):
            if((sd[j]<sd[k] and cd[j]>cd[k]) or (sd[j]>sd[k] and cd[j]<cd[k])):
                ans = ans + 1

    print "Case #{}: {}".format(i,ans)






