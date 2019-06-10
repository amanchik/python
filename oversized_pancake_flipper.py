t = int(raw_input()) # read a line with a single integer
def flip(c):
    if c == '+':
        return  '-'
    else:
        return  '+'
for i in xrange(1, t + 1):
    s,k = raw_input().split(" ")
    k = int(k)
    s = list(s)
    p = 0
    l = len(s)
    finished = False
    ans = 0
    while p+k-1<l:
        while s[p] == '+':
            p += 1
            if p == l:
                finished = True
                break
        if finished:
            break
        if p+k-1 >= l:
            break
        for j in range(k):
            s[p+j]=flip(s[p+j])
        ans += 1
    if finished:
        print "Case #{}: {}".format(i, ans)
    else:
        print "Case #{}: IMPOSSIBLE".format(i)