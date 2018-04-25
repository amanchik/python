import sys
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
def lcm(a,b):
    return (a*b)/hcf(a,b)
def calc(b,n,bs,mm):
        tops = []
        m = 0
        while True:
            for j in range(b):
                tops.append((m * bs[j], j))
            m = m + 1
            if m > mm:
                break
        stops = sorted(tops, key=lambda element: (element[0], element[1]))
       # print stops
        return stops[n-1][1]+1

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    b,n = [int(s) for s in raw_input().split(" ")]
    bs = [int(s) for s in raw_input().split(" ")]

    lm = 1

    for j in range(b):
        lm = lcm(lm,bs[j])


    ccount = 0
    minb = 100001
    for x in bs:
        ccount = ccount + (lm/x)
        if x < minb:
            minb = x

   # print ccount
    if n%ccount == 0:
        n = ccount
    else:
        n =  n%ccount
       # print stops

    print "Case #{}: {}".format(i, calc(b,n,bs,lm/minb))
    sys.stdout.flush()







