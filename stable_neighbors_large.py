import random
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,r,o,y,g,b,v = [int(s) for s in raw_input().split(" ")]
    if r != 0 and g != 0 and o == 0 and y == 0  and b == 0 and v == 0 and r == g:
        ans = ['RG' for j in range(r)]
        print "Case #{}: {}".format(i,''.join(ans))
    elif r == 0 and g == 0 and o == 0 and y != 0  and b == 0 and v != 0 and y == v:
        ans = ['YV' for j in range(y)]
        print "Case #{}: {}".format(i,''.join(ans))
    elif r == 0 and g == 0 and o != 0 and y == 0 and b != 0 and v == 0 and b == o:
        ans = ['BO' for j in range(b)]
        print "Case #{}: {}".format(i, ''.join(ans))
    elif (g==0 or r > g) and (v==0 or y>v) and (o==0 or b>o):
       # print r,o,y,g,b,v
        rc = r
        yc = y
        bc = b
        r = r - g
        y = y - v
        b = b - o
        nm = r + y + b
        if r>nm/2 or y>nm/2 or b>nm/2:
            print "Case #{}: IMPOSSIBLE".format(i)
        else:
            maxR = False
            if r>=y and r>b:
                maxR = True
            maxY =  False
            if y>=r and y>=b:
                maxY = True
            ans = ['-' for j in range(nm)]
            start = 0
            while r>0 or y>0 or b>0:
                if r>0 and maxR:
                    ans[start]='R'
                    start = start + 2
                    if start == nm or start == nm+1:
                        start = 1
                    r = r - 1
                    if r == 0:
                        maxY = True
                   #     start = start - 1
                elif y>0 and maxY:
                    ans[start] = 'Y'
                    start = start + 2
                    if start == nm or start == nm+1:
                        start = 1
                    y = y-1
                    if y == 0:
                        maxR = True
                     #   start = start - 1
                elif b>0:
                    ans[start] = 'B'
                    start = start + 2
                    if start == nm or start == nm+1:
                        start = 1
                    b = b - 1
                    if b == 0:
                        maxY = True
                        maxR = True
            if g>0 :
                ans[ans.index('R')] = ''.join(['RG' for k in range(g)]) + 'R'
            if v>0 :
                ans[ans.index('Y')] = ''.join(['YV' for k in range(v)]) + 'Y'
            if o>0 :
                ans[ans.index('B')] = ''.join(['BO' for k in range(o)]) + 'B'
            ans = ''.join(ans)
            if rc != ans.count('R'):
                print  "break R " + str(ans.count('R'))
            if bc != ans.count('B'):
                print  "break B "+ str(ans.count('B'))
            if yc != ans.count('Y'):
                print  "break Y "+ str(ans.count('Y'))
            if g != ans.count('G'):
                print  "break G "+ str(ans.count('G'))
            if v != ans.count('V'):
                print  "break V "+ str(ans.count('V'))
            if o != ans.count('O'):
                print  "break O "+ str(ans.count('O'))
            print "Case #{}: {}".format(i,ans)
    else:
        print "Case #{}: IMPOSSIBLE".format(i)
