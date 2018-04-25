import random
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,r,o,y,g,b,v = [int(s) for s in raw_input().split(" ")]
    if r>n/2 or y>n/2 or b>n/2:
        print "Case #{}: IMPOSSIBLE".format(i)
    else:
        maxR = False
        if r>=y and r>b:
            maxR = True
        maxY =  False
        if y>=r and y>=b:
            maxY = True
        ans = ['-' for j in range(n)]
        start = 0
        while r>0 or y>0 or b>0:
            if r>0 and maxR:
                while ans[start] != '-':
                    start = start + 1
                    start = start % n
                ans[start]='R'
                start = start + 2
                start = start%n
                r = r - 1

                if r == 0:
                    maxY = True
               #     start = start - 1
            elif y>0 and maxY:
                while ans[start] != '-':
                    start = start + 1
                    start = start%n
                ans[start] = 'Y'
                start = start + 2
                start = start % n
                y = y-1
                if y == 0:
                    maxR = True
                 #   start = start - 1
            elif b>0:
                while ans[start] != '-':
                    start = start + 1
                    start = start%n
                ans[start] = 'B'
                start = start + 2
                start = start % n
                b = b -1
                if b == 0:
                    maxY = True
                    maxR = True
        if ans[0] == ans[-1]:
            print  "break"
        print "Case #{}: {}".format(i,''.join(ans))
