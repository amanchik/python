import sys

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,x= [int(s) for s in raw_input().split(" ")]
    s =  [int(s) for s in raw_input().split(" ")]
    s.sort()
    s = s[::-1]
    ans = 0
    while len(s) > 0 :
        not_found = True
        for j in range(1,len(s)):
            if s[0] + s[j] <= x:
                del s[j]
                del s[0]
                ans = ans + 1
                not_found = False
                break
        if not_found:
            del s[0]
            ans = ans + 1



    print "Case #{}: {}".format(i,ans)
    sys.stdout.flush()




