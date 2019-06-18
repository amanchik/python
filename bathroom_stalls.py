t = int(raw_input()) # read a line with a single integer
def split(m):
    n = m[0]
    if n == 2:
        return  [(1,m[1])]
    if n%2 == 0:
        return  [(n/2-1,m[1]),(n/2,m[1])]
    else:
        return  [((n-1)/2,2*m[1])]
def merge_list(l):
    ans = {}
    for x in l:
        if x[0] in ans:
            ans[x[0]] += x[1]
        else:
            ans[x[0]] = x[1]
    return sorted([(x,ans[x]) for x in ans], key=lambda x: x[0])

for i in xrange(1, t + 1):
    n,k =  [int(s) for s in raw_input().split(" ")]
    first_list =  split((n,1))
    first_merge = merge_list(first_list)
  #  print  first_merge
    k -= 1
    while len(first_merge) > 1 or first_merge[0][0] != 1:
        if len(first_merge) == 1:
            if k > first_merge[0][1]:
                k -= first_merge[0][1]
            else:
                break
        elif k > first_merge[0][1] + first_merge[1][1]:
            k -= first_merge[0][1] + first_merge[1][1]
        else:
            break
        tmp = []
        for x in first_merge:
            if x[0] > 1:
                tmp.extend(split(x))
            else:
                tmp.append(x)
        first_merge = merge_list(tmp)
      #  print first_merge,k

    ans = 1
    if len(first_merge) == 1 and first_merge[0][0]==1 and k != 0:
        ans = 1
    elif k == 0:
        ans = n
    else:
        if len(first_merge) == 1:
            ans = first_merge[0][0]
        elif k <= first_merge[1][1]:
            ans = first_merge[1][0]
        else:
            ans = first_merge[0][0]
    if ans%2 == 0:
        print "Case #{}: {} {}".format(i,ans/2,ans/2-1)
    else:
        print "Case #{}: {} {}".format(i, (ans-1) / 2, (ans-1) / 2)






    #    print first_merge