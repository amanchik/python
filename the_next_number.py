

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()
    s = list(s)
    index = -1
    for j in reversed(range(len(s))):
        if j>0 and int(s[j])>int(s[j-1]):
            index = j-1
            break
    if index != -1:
        sindex = index + 1
        min_d = int(s[sindex])
        for j in range(sindex,len(s)):
            if int(s[j]) > int(s[index]) and int(s[j])<min_d:
                min_d = int(s[j])
                sindex = j
        tmp = s[sindex]
        s[sindex] = s[index]
        s[index] = tmp
        ans = s[0:index+1] + sorted(s[index+1:])
    else:
        min_d = 9
        index = 0
        for j in range(len(s)):
            if int(s[j]) < min_d and int(s[j])>0:
                min_d = int(s[j])
                index = j
        del s[index]
        ans = [str(min_d),'0'] + sorted(s)
    print "Case #{}: {}".format(i,''.join(ans))



