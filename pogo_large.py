def is_square(n):
    sq = n**0.5
    if sq*sq == n:
        return True
    else:
        return False


#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    x,y = [int(s) for s in raw_input().split(" ")]
    negative_x = False
    negative_y = False
    if x<0:
        negative_x = True
        x = -1*x
    if y<0:
        negative_y= True
        y = -1*y

    n = ((8*(x+y)+1)**0.5 - 1 )/2
    n = int(n)
    max_n = n + 3
    toggle = -2
    if n*(n+1)/2 != x + y and x+y>2:
        n = n + 1
        toggle = ((n*(n+1)/2)-(x+y))
        if toggle % 2 == 1:
            n = n + 1
            toggle = ((n * (n + 1) / 2) - (x + y))
            if toggle % 2 == 1:
                n = n + 1
                toggle = ((n * (n + 1) / 2) - (x + y))

    tx = 0
    ty = 0
    xs = []
    ys = []
    nra = list(range(1,n+1))
    nra = nra[::-1]
    if toggle>0:
        if toggle < 2*n:
            nra[nra.index(toggle/2)] = -1*(toggle/2)
        else:
            findr = toggle/2
            if findr%2 == 0 :
                a = (findr/2) + 1
                b = (findr/2) - 1
            else:
                a = (findr / 2) + 1
                b = (findr / 2)
            nra[nra.index(a)] = -1 * a
            nra[nra.index(b)] = -1 * b

    skip = -1
    for j in nra:
        if skip >= 0 and skip != j:
            ty += j
            ys.append(j)
        if skip == -1 and tx < x:
            tx += j
            xs.append(j)
        if skip == -1 and tx == x:
            skip = 0
            if x == 0:
                ty += j
                ys.append(j)

        if skip == -1 and tx > x:
            skip = j - (tx - x)
            tx = x
            ty = j
            del xs[-1]
            xs.append(skip)
            ys.append(j)

  #  print x,y
  #  print tx,ty
  #  print n
  #  print toggle
    ans = ''
    for j in reversed(nra):
        if j in xs:
            if j<0:
                if negative_x:
                    ans += 'E'
                else:
                    ans += 'W'
            else:
                if negative_x:
                    ans += 'W'
                else:
                    ans += 'E'
        else:
            if j<0:
                if negative_y:
                    ans += 'N'
                else:
                    ans += 'S'
            else:
                if negative_y:
                    ans += 'S'
                else:
                    ans += 'N'
    if tx < x :
        if negative_x:
            ans += 'EW'
        else:
            ans += 'WE'
    elif tx > x:
        if negative_x:
            ans += 'WE'
        else:
            ans += 'EW'

    if ty < y :
        if negative_y:
            ans += 'NS'
        else:
            ans += 'SN'
    elif ty > y:
        if negative_y:
            ans += 'SN'
        else:
            ans += 'NS'
    '''
    if n != len(ans):
        print "what"
        print n, len(ans)
        print x,y
        print tx,ty
        print n
        print toggle
    '''
    if len(ans) > max_n:
        print "check "+str(len(ans))
    lans = list(ans)
    ttx = 0
    tty = 0
    current = 1
    for l in lans:
        if l=='E':
            ttx += current
        elif l=='W':
            ttx -= current
        elif l=='N':
            tty += current
        else:
            tty -= current
        current += 1
    if ttx<0:
        ttx = -1*ttx
    if tty<0:
        tty = -1*tty
    if x != ttx or y != tty:
        print "chekc "+str(ttx)+" "+str(tty)

  #  print xs
   # print ys
    print "Case #{}: {}".format(i,ans)



