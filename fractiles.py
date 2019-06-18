t = int(raw_input()) # read a line with a single integer
def get_index(v,n):
    n_r = [n**j for j in reversed(range(len(v)))]
    zero = [x-1 for x in v]
    prod = [a*b for a,b in zip(n_r,zero)]
    return  sum(prod) + 1

for i in xrange(1, t + 1):
    k,c,s =  [int(s) for s in raw_input().split(" ")]
    if c==1 and k != s:
        print "Case #{}: IMPOSSIBLE".format(i)
    elif c==1:
        ans = range(1,k+1)
        ans = [str(x) for x in ans]
        print "Case #{}: {}".format(i,' '.join(ans))
    else:
        if c > k:
            c = k
        r = k/c
        if k%c != 0:
            r += 1
        if s < r:
            print "Case #{}: IMPOSSIBLE".format(i)
        else:
           ans = []
           j = 0
           st = 1
           while j < r :
               v = [p+st for p in range(c)]
               if v[-1] > k :
                   diff = v[-1]-k
                   v = [x-diff for x in v]
               ans.append(get_index(v,k))
               j += 1
               st += c
           ans = [str(x) for x in ans]
           print "Case #{}: {}".format(i,' '.join(ans))