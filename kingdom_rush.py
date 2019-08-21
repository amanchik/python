t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    r1 = []
    r2 = []
    N = int(raw_input())
    for j in range(N):
        a, b = [int(s) for s in raw_input().split(" ")]
        r1.append((j,b,a))
        r2.append((j,b,a))
    sr1 = sorted(r1, key=lambda x: x[1])
    sr2 = sorted(r2, key=lambda x: x[1])
  #  print sr1,sr2


    solvedA = {}
    solvedB = {}
    ans = 0
    count = 0
    too_bad = False
    start = 0
    for (x,y,z) in sr2:
     #   print start, ans,solvedA, solvedB
        if ans >= y:
            solvedB[x] = True
            if x in solvedA:
                ans += 1
            else:
                ans += 2
            count += 1
        else:

            while ans < y:
                never = True
                for (u,v,w) in reversed(sr1):
                    if w<=ans and u not in solvedB and u not  in solvedA:
                        ans += 1
                        count += 1
                        solvedA[u] = True
                        never = False
                        break
                if ans >= y:
                    break
                if never:
                #    print ans,solvedA,solvedB
                    break

            if ans < y:
                too_bad = True
                break
            else:
                solvedB[x] = True
                if x in solvedA:
                    ans += 1
                else:
                    ans += 2
                count += 1


    if too_bad:
        print "Case #{}: {}".format(i, "Too Bad")
    else:
        print "Case #{}: {}".format(i, str(count))