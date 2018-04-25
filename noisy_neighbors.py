def get_ans(r,c,n,trick):
    occupied = [[True for j in range(c)] for k in range(r)]
    if trick:
        for j in range(r):
            for k in range(c):
                if j % 2 == 0 and k % 2 == 0:
                    occupied[j][k] = False
                elif j % 2 == 1 and k % 2 == 1:
                    occupied[j][k] = False
                else:
                    n = n - 1
    else:
        for j in range(r):
            for k in range(c):
                if j % 2 == 0 and k % 2 == 1:
                    occupied[j][k] = False
                elif j % 2 == 1 and k % 2 == 0:
                    occupied[j][k] = False
                else:
                    n = n - 1
    #  print occupied
    # print n

    over = False
    for j in range(r):
        if over:
            break
        for k in range(c):
            if (k == 0 and j == 0) or (k == c - 1 and j == r - 1) or (k == 0 and j == r - 1) or (j == 0 and k == c - 1):
                if (not occupied[j][k]) and n > 0:
                    occupied[j][k] = True
                    n -= 1
                elif n == 0:
                    over = True
                    break
    for j in range(r):
        if over:
            break
        for k in range(c):
            if k == 0 or j == 0 or k == c - 1 or j == r - 1:
                if (not occupied[j][k]) and n > 0:
                    occupied[j][k] = True
                    n -= 1
                elif n == 0:
                    over = True
                    break
    # print n

    for j in range(r):
        if over:
            break
        for k in range(c):
            if (not occupied[j][k]) and n > 0:
                occupied[j][k] = True
                n -= 1
            elif n == 0:
                over = True
                break
    #     print n
    #     print occupied
    ans = 0
    for j in range(r):
        for k in range(c):
            if occupied[j][k]:
                if j > 0 and occupied[j - 1][k]:
                    ans += 1
                if j + 1 < r and occupied[j + 1][k]:
                    ans += 1
                if k > 0 and occupied[j][k - 1]:
                    ans += 1
                if k + 1 < c and occupied[j][k + 1]:
                    ans += 1
    return ans

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    r,c,n = [int(s) for s in raw_input().split(" ")]

    zeros = 0
    for j in range(r):
        if j%2 == 0 and c%2==1:
            zeros += (c/2)+1
        else:
            zeros += (c/2)
    if n<=zeros:
        print "Case #{}: {}".format(i, 0)
    else:
        ans1 = get_ans(r,c,n,False)
        ans2 = get_ans(r,c,n,True)
        ans = ans1
        if ans2 < ans1:
            ans = ans2
        print "Case #{}: {}".format(i,ans/2)



