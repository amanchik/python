def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
def adjacent(m,n,r,c,):
    i = m/c
    j = m%c
    if j + 1 < c and c*i + j+1 == n:
        return True
    if j > 0 and c*i + j-1 == n:
        return True
    if i + 1 < r and c*(i+1)+j == n:
        return True
    if i > 0 and c*(i-1)+j==n:
        return True
    if i > 0 and j > 0 and c*(i-1)+j-1==n:
        return True
    if j + 1 < c and i + 1 < r and c*(i+1)+j+1==n:
        return True
    if i > 0 and j + 1 < c and c*(i-1)+j+1==n:
        return True
    if i + 1 < r and j > 0 and c*(i+1)+j-1==n:
        return True
    return False
def adjacent_minus_one(m,r,c,i,j):
    if j + 1 < c and m[i][j + 1] == -1:
        return True
    if j > 0 and m[i][j - 1] == -1:
        return True
    if i + 1 < r and m[i + 1][j] == -1:
        return True
    if i > 0 and m[i - 1][j] == -1:
        return True
    if i > 0 and j > 0 and m[i - 1][j - 1] == -1:
        return True
    if j + 1 < c and i + 1 < r and m[i + 1][j + 1] == -1:
        return True
    if i > 0 and j + 1 < c and m[i - 1][j + 1] == -1:
        return True
    if i + 1 < r and j > 0 and m[i + 1][j - 1] == -1:
        return True
    return False
def span_from_recursive(m,r,c,i,j):
    if j + 1 < c and m[i][j + 1] == 0:
            m[i][j+1] = -1
            span_from_recursive(m,r,c,i,j+1)
    if j > 0 and m[i][j - 1] == 0:
            m[i][j - 1] = -1
            span_from_recursive(m,r,c,i,j-1)
    if i + 1 < r and m[i + 1][j] == 0:
            m[i + 1][j] = -1
            span_from_recursive(m,r,c,i+1,j)
    if i > 0 and m[i - 1][j] == 0:
            m[i - 1][j] = -1
            span_from_recursive(m,r,c,i-1,j)
    if i > 0 and j > 0 and m[i - 1][j - 1] == 0:
            m[i - 1][j - 1] = -1
            span_from_recursive(m,r,c,i-1,j-1)
    if j + 1 < c and i + 1 < r and m[i + 1][j + 1] == 0:
            m[i + 1][j + 1] = -1
            span_from_recursive(m,r,c,i+1,j+1)
    if i > 0 and j + 1 < c and m[i - 1][j + 1] == 0:
            m[i - 1][j + 1] = -1
            span_from_recursive(m,r,c,i-1,j+1)
    if i + 1 < r and j > 0 and m[i + 1][j - 1] == 0:
            m[i + 1][j - 1] = -1
            span_from_recursive(m,r,c,i+1,j-1)

def span_from(m,r,c,i,j):
    m[i][j] = -1
    span_from_recursive(m,r,c,i,j)
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
    first = first_zero(m,r,c)
    span_from(m,r,c,first/c,first%c)
    first = first_zero(m,r,c)
    if first != -1:
        return False
    else:
      #  print m
        return True


    #print m

def fill(r,c,bombs):
    ans = [['.' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if i*c + j in bombs:
                ans[i][j] = '*'
    return ans
def first_zero(m,r,c):
    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                return c*i + j
    return -1
def first_minus(m,r,c):
    for i in range(r):
        for j in range(c):
            if m[i][j] == -1:
                return c*i + j
    return -1



def print_all(y):
    for x in y:
        print x
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    r, c, m = [int(s) for s in raw_input().split(" ")]
    print "Case #{}:".format(i)
    not_printed = True
    y = combinations(range(r*c), m)
    for x in y:
        ans = fill(r,c,x)
       # print ans
        if calc(ans,r,c):
            #print ans
            first = first_minus(ans,r,c)
            res = []
            for row in ans:
                s = ['.' if isinstance(k,int) else k for k in row]
                res.append(s)
            res[first/c][first%c] = 'c'
               # print  ''.join(s)
            for s in res:
                print ''.join(s)
            not_printed = False
            break
    if  m == r*c-1:
        res = [['*' for k in range(c)] for j in range(r)]
        res[0][0] = 'c'
        for s in res:
            print ''.join(s)
    elif not_printed:
        print  "Impossible"





