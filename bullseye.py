def square_root(n):
    x = n
    y = (x+ n/x)/2;
    while y<x:
        x = y
        y = (x + n/x)/2
    return x


T = raw_input("")
T = int(T)
for c in range(1,T+1):
    line = raw_input()
    parts = line.split()
    r = long(parts[0])
    t = long(parts[1])
    right = square_root(8*t+(2*r-1)**2)
    ans = (right+1-2*r)/4
    print "Case #"+str(c)+": "+str(ans)
