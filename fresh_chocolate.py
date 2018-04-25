

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,p = [int(s) for s in raw_input().split(" ")]
    g = [int(s) for s in raw_input().split(" ")]

    rg = [x%p for x in g]
    rg.sort()
    ans = 0
    while len(rg)>0:
        if 0 in rg:
            index = rg.index(0)
            ans += 1
            del rg[index]
        elif 1 in rg and (p-1) in rg and 1 != p-1:
            index1 = rg.index(1)
            del rg[index1]
            index2 = rg.index(p-1)
            del rg[index2]
            ans += 1
        else:
            if p<=3:
                ans += len(rg)/p
                if len(rg)%p != 0:
                    ans += 1
                break
            else:
                count = rg.count(2)
                ans+= (count/2)
                count = count - (count%2)
                while count>0:
                    index1 = rg.index(2)
                    del rg[index1]
                    count -= 1
                if 2 in rg and  rg.count(1)>1:
                    index1 = rg.index(2)
                    del rg[index1]
                    index1 = rg.index(1)
                    del rg[index1]
                    index1 = rg.index(1)
                    del rg[index1]
                    ans += 1
                if 1 in rg and 2 in rg:
                    ans += 1
                    break
                if 1 in rg:
                    ans += (rg.count(1)/4)
                    if len(rg) % p != 0:
                        ans += 1
                    break
                ans += (rg.count(3) / 4)
                if len(rg) % p != 0:
                    ans += 1
                break





    print "Case #{}: {}".format(i,ans)



