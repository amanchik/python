def hcf(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a%b == 0:
        return b
    elif b%a == 0:
        return a
    elif a>b:
        return hcf(b,a%b)
    else:
        return hcf(a,b%a)
def mod(a,b):
    if a>b:
        return a-b
    else:
        return b-a
#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    l = [int(s) for s in raw_input().split(" ")]
    l = l[1:]
    diffs = []
    for j in range(len(l)):
        for k in range(0,j):
            diffs.append(mod(l[j],l[k]))
    score = -1
    for j in range(len(diffs)):
       if score == -1:
           score = diffs[j]
       else:
           score = hcf(score,diffs[j])
    if l[0]%score == 0:
        print "Case #{}: 0".format(i)
    else:
        print "Case #{}: {}".format(i,score-l[0]%score)





