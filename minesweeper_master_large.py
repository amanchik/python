def calc(m,r,c):
    for i in range(r):
        for j in range(c):
            if m[i][j] != '*':
                ans = 0
                if j+1<c and m[i][j+1] == '*':
                    ans += 1
                if j>0 and m[i][j-1] == '*':
                    ans += 1
                if i+1<r and m[i+1][j] == '*':
                    ans += 1
                if i>0 and m[i-1][j] == '*':
                    ans += 1
                if i>0 and j>0 and m[i-1][j-1] == '*':
                    ans += 1
                if j+1<c and i+1<r and m[i+1][j+1] == '*':
                    ans += 1
                if i>0 and j+1<c and m[i-1][j+1] == '*':
                    ans += 1
                if i+1<r and j>0 and m[i+1][j-1] == '*':
                    ans += 1
                m[i][j] = ans
    failed = False
    for i in range(r):
        if not failed:
            for j in range(c):
                if m[i][j]=='*' or m[i][j]==0:
                    continue
                if j + 1 < c and m[i][j + 1] == 0 :
                    continue
                if j > 0 and m[i][j - 1] == 0:
                    continue
                if i + 1 < r and m[i + 1][j] == 0:
                    continue
                if i > 0 and m[i - 1][j] == 0:
                    continue
                if i > 0 and j > 0 and m[i - 1][j - 1] == 0:
                    continue
                if j + 1 < c and i + 1 < r and m[i + 1][j + 1] == 0:
                    continue
                if i > 0 and j + 1 < c and m[i - 1][j + 1] == 0:
                    continue
                if i + 1 < r and j > 0 and m[i + 1][j - 1] == 0:
                    continue
                failed = True
                break
    if failed:
        return False
    else:
      #  print m
        return True


    #print m






def print_all(y):
    for x in y:
        print x
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    r, c, m = [int(s) for s in raw_input().split(" ")]
    print "Case #{}:".format(i)
    if r==1 or c==1 or r*c-1 == m or m==0:
        if r==1:
            ans = ['*' if j<m else '.' for j in range(c)]
            ans[-1] = 'c'
            print ''.join(ans)
        elif c==1:
            ans = ['*' if j < m else '.' for j in range(r)]
            ans[-1] = 'c'
            for x in ans:
                print x
        elif r*c-1==m:
            ans = [['*' for j in range(c)] for k in range(r)]
            ans[-1][-1]='c'
            for x in ans:
                print ''.join(x)
        elif m==0:
            ans = [['.' for j in range(c)] for k in range(r)]
            ans[-1][-1] = 'c'
            for x in ans:
                print ''.join(x)
    elif r==2 or c==2:
        if m%2==1 or (r*c-m)==2:
            print "Impossible"
        else:
            if r==2:
                ans = [['*' if j<m/2 else '.' for j in range(c)] for k in range(2)]
                ans[-1][-1]='c'
                for x in ans:
                    print ''.join(x)
            else:
                ans = [['*' for k in range(2)] if j<m/2 else ['.' for k in range(2)] for j in range(r)]
                ans[-1][-1] = 'c'
                for x in ans:
                    print ''.join(x)
    else:
        e = r*c - m
        if e < 9:
            if (e%2 == 1 or e==2):
                print "Impossible"
            else:
                tm = m
                ans = [['.' for j in range(c)] for k in range(r)]
                for j in range(r):
                    for k in range(c):
                        if j < (r - 2) and tm > 0:
                            ans[j][k] = '*'
                            tm = tm - 1
                for k in range(c):
                    if tm > 1:
                        ans[-1][k] = '*'
                        ans[-2][k] = '*'
                        tm = tm - 2
                ans[-1][-1] = 'c'
                for x in ans:
                    print ''.join(x)
        else:
            if e>=3*c:
                tm = m
                ans = [['.' for j in range(c)] for k in range(r)]
                for j in range(r):
                    for k in range(c):
                        if tm > 1:
                            ans[j][k] = '*'
                            tm = tm - 1
                        elif tm == 1:
                            if k==c-2:
                                ans[j+1][0] = '*'
                            else:
                                ans[j][k] = '*'
                            tm = tm -1
                ans[-1][-1] = 'c'
                for x in ans:
                    print ''.join(x)
            else:
                tm = m
                ans = [['.' for j in range(c)] for k in range(r)]
                for j in range(r):
                    for k in range(c):
                        if j<(r-3):
                            ans[j][k] = '*'
                            tm = tm - 1
                for k in range(c):
                    if tm > 1 :
                        ans[-3][k] = '*'
                        tm = tm - 1
                    elif tm>0:
                        ans[-3][k] = '*'
                        tm = tm - 1
                    if tm > 1:
                        ans[-2][k] = '*'
                        tm = tm - 1
                    elif tm > 0:
                        ans[-3][k+1] = '*'
                        tm = tm - 1
                    if tm > 1:
                        ans[-1][k] = '*'
                        tm = tm - 1
                    elif tm > 0:
                        ans[-1][k] = '*'
                        tm = tm - 1
                ans[-1][-1] = 'c'
                for x in ans:
                    print ''.join(x)
