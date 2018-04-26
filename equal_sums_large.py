import sys
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

#print pi
t = int(raw_input()) # read a line with a single integer

for i in xrange(1, t + 1):
    s = [int(s) for s in raw_input().split(" ")]
    n=s[0]
    s=s[1:]
    s.sort()
    diffs = []
    for j in range(1,n):
        diff = (s[j] - s[j-1],(j,1-j))
        diffs.append(diff)
    while len(diffs)>1:
        tmp = []
        diffs.sort(key=lambda x: x[0])
        for j in range(1, len(diffs)):
            diff = (diffs[j][0]-diffs[j-1][0],diffs[j][1]+tuple([-1*x for x in diffs[j-1][1]]))
            tmp.append(diff)
        diffs = tmp
        found_ans = False
        for (x,y) in diffs:
            if x == 0 and len(y)==len(set(y)):
                ans = y
                found_ans = True
                break
        if found_ans:
            break
   # print ans
    ans1 = [ans[j] for j in range(len(ans)) if ans[j] > 0]
    ans2 = [ans[j] for j in range(len(ans)) if ans[j] < 0]
    ans1 = [s[x] for x in ans1]
    ans2 = [s[-1*x] for x in ans2]
    if len(set(ans1))+len(set(ans2)) != len(set(ans1+ans2)):
        dups = []
        for x in ans1:
            if x in ans2:
                dups.append(x)
        ans1 = [x for x in ans1 if x not in dups]
        ans2 = [x for x in ans2 if x not in dups]
    '''
    if len(ans1) != len(set(ans1)):
        print "alternate"
    if sum(ans1) == sum(ans2):
        print "yes"
        print sum(ans1)
    '''
    print "Case #{}:".format(i)
    print ' '.join([str(x) for x in ans1])
    print ' '.join([str(x) for x in ans2])
    sys.stdout.flush()




