

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()
    su = set(list(s))
    mapping = {}
    mapping[s[0]]=1
    current = 0
    for x in s:
        if x not in mapping:
            mapping[x]=current
            if current == 0:
                current += 2
            else:
                current += 1
    base = 2
    if len(su)>2:
        base = len(su)
    ans = 0
    for j in range(len(s)):
        ans += mapping[s[j]]*(base**(len(s)-1-j))

    print "Case #{}: {}".format(i,ans)



