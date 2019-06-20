import  sys
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

def sum_base(n,k):
     ans = 0
     while n>0:
         remainder = n%k
         ans += remainder*remainder
         n = n/k
     return ans
# def sum_base(n,k):
#     n = base(n,k)
#     ans = 0
#     for x in n:
#         ans += int(x)*int(x)
#     return ans
def base(n,k):
    if k == 10:
        return str(n)
    ans = []
    while n>0:
        ans.append(str(n%k))
        n = n/k
    return ''.join(reversed(ans))
  #  if n == 0:
  #      return s
  #  else:
  #      return  base(n/k,k,str(n%k)+s)

mapping = {}
for k in range(2,11):
    mapping[k] = {}
    for j in range(1,1000):
        mapping[k][j]=sum_base(j,k)
#print mapping
def is_one(n,k,count):
    if mapping[k][n] == 1:
        return True
    if count > 10:
        return False
    return is_one(mapping[k][n],k,count+1)
reduced_one = {}
for k in range(2,11):
    reduced_one[k] = {}
    for j in range(1,1000):
        reduced_one[k][j] = is_one(j,k,0)



cached_ans = {}
count = 2
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    ar = raw_input().split(" ")

    se = ''.join(ar)
    if se not in cached_ans:
        while True:

            tmp = ''
            for k in range(2,11):
                basic = sum_base(count, k)
                if reduced_one[k][basic]:
                   tmp += str(k)
            se_ii = tmp

            if se_ii not in cached_ans:
                for j in range(1,len(tmp)+1):
                    for x in combinations(tmp,j):
                        se_i = ''.join(x)
                        if se_i not in cached_ans:
                            cached_ans[se_i] = count
            sys.stderr.write(str(count)+'\n')

            count += 1
            if se in cached_ans:
                break
    print "Case #{}: {}".format(i, cached_ans[se])




