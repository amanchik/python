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
    found_answer = False
    allsums = [x for x in s]
    number_so_far = n
    ans = -1
    for j in range(2,(n/2)+1):
        if found_answer:
            break
        indexes = combinations(range(n),j)
        for index in indexes:
            if found_answer:
                break
            sum_to_find = sum([s[x] for x in index])
            allsums.append(sum_to_find)
            number_so_far += 1
        if len(allsums) != len(set(allsums)):
            ans = -1
            for x in set(allsums):
                if allsums.count(x)>1:
                    ans = x
                    break
          #  print ans
            found_answer = True
            break
    found_answers = 0
    for j in range(1,(n/2)+1):
        if found_answers == 2:
            break
        indexes = combinations(range(n),j)
        for index in indexes:
            if found_answers == 2:
                break
            ansx = [s[x] for x in index]
            sum_to_find = sum(ansx)
            if sum_to_find == ans:
                found_answers += 1
                if found_answers == 1 :
                    ans1 = ansx
                elif found_answers == 2:
                    ans2 = ansx





    print "Case #{}:".format(i)
    print ' '.join([str(x) for x in ans1])
    print ' '.join([str(x) for x in ans2])
    sys.stdout.flush()




