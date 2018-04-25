

t = int(raw_input()) # read a line with a single integer
for tt in xrange(1, t + 1):
    r, c, h,v = [int(s) for s in raw_input().split(" ")]
    # include <iostream>
    s = []
    for i in range(r):
        s.append(raw_input())

    product = (h+1) * (v+1);
    total = 0
    rows = [0 for i in range(r)]
    cols = [0 for i in range(c)]
    for i in range(r):
        for j in range(c):
            if s[i][j] == '@' :
                rows[i] = rows[i] + 1
                cols[j] = cols[j] + 1
                total = total + 1
    ch = [0 for i in range(h)]
    cv = [0 for i in range(v)]

    if total == 0:
        print "Case #{}: POSSIBLE".format(tt)
    elif total%product == 0:
        box = total/product
        prow = total / (h+1)
        pcol = total / (v+1)
        failed = False
        rem = prow
        current  = 0
        for i in range(r):
            if rows[i] > rem:
                failed = True
                break
            elif rows[i] == rem:
                rem = prow
                if current<h:
                    ch[current] = i
                current = current + 1
            else:
                rem = rem - rows[i]
        rem = pcol
        current = 0
        for i in range(c):
            if cols[i] > rem:
                failed = True
                break
            elif cols[i] == rem:
                rem = pcol
                if current<v:
                    cv[current] = i
                current = current + 1
            else:
                rem = rem - cols[i]
        if failed:
            print "Case #{}: IMPOSSIBLE".format(tt)
        else:
            starti = 0
            startj=0
            for i in range(h):
                endi = ch[i]
                for j in range(v):
                    endj = cv[j]
                    count  = 0
                    for m in range(starti,endi+1):
                        for n in range(startj,endj+1):
                            if s[m][n]=='@':
                                count = count + 1
                    if count != box:
                        failed = True
                        break
                    startj = endj + 1
                if failed:
                    break
                starti = ch[i] + 1
                startj = 0
            if failed:
                print "Case #{}: IMPOSSIBLE".format(tt)
            else:
                print "Case #{}: POSSIBLE".format(tt)
    else:
        print "Case #{}: IMPOSSIBLE".format(tt)








