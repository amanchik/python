

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,kk = [int(s) for s in raw_input().split(" ")]
    board = []
    for j in range(n):
        top = list(raw_input())
        if 'R' in top or 'B' in top:
            chs = [x for x in top if x!='.']
            dots = [x for x in top if x=='.']
            top = dots + chs
        board.append(top)

    #for x in board:
    #    print ''.join(x)

    rboard = []
    for j in range(n):
        col = [x[j] for x in board]
        col = col[::-1]
        rboard.append(col)

   # for x in rboard:
   #     print ''.join(x)
    red = False
    blue = False
    for j in range(n):
        for k in range(n):
            startx = j
            starty = k
            count = 0
            while startx<n and starty<n and rboard[startx][starty]=='R':
                count += 1
                startx += 1
            if count >= kk:
                red = True
            startx = j
            starty = k
            count = 0
            while startx < n and starty < n and rboard[startx][starty] == 'R':
                count += 1
                starty += 1
            if count >= kk:
                red = True
            startx = j
            starty = k
            count = 0
            while startx < n and starty < n and rboard[startx][starty] == 'R':
                count += 1
                startx += 1
                starty += 1
            if count >= kk:
                red = True


            startx = j
            starty = k
            count = 0
            while startx>=0 and startx < n and starty < n and rboard[startx][starty] == 'R':
                count += 1
                startx -= 1
                starty += 1
            if count >= kk:
                red = True

            startx = j
            starty = k
            count = 0
            while startx < n and starty < n and rboard[startx][starty] == 'B':
                count += 1
                startx += 1
            if count >= kk:
                blue = True
            startx = j
            starty = k
            count = 0
            while startx < n and starty < n and rboard[startx][starty] == 'B':
                count += 1
                starty += 1
            if count >= kk:
                blue = True
            startx = j
            starty = k
            count = 0
            while startx < n and starty < n and rboard[startx][starty] == 'B':
                count += 1
                startx += 1
                starty += 1
            if count >= kk:
                blue = True

            startx = j
            starty = k
            count = 0
            while startx>=0 and startx < n and starty < n and rboard[startx][starty] == 'B':
                count += 1
                startx -= 1
                starty += 1
            if count >= kk:
                blue = True
    if red and blue:
        print "Case #{}: Both".format(i)
    elif red:
        print "Case #{}: Red".format(i)
    elif blue:
        print "Case #{}: Blue".format(i)
    else:
        print "Case #{}: Neither".format(i)




