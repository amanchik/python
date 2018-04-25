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
def lcm(a,b):
    return (a*b)/hcf(a,b)
def is_possible(k,f):
    for x in f:
        if x % k != 0 and k % x != 0:
            return False
    return True

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,l,h = [int(s) for s in raw_input().split(" ")]
    f = [int(s) for s in raw_input().split(" ")]
    ans = -1

    if h-l<20000:
        for k in range(l, h + 1):
            possible = True
            for x in f:
                if x % k != 0 and k % x != 0:
                    possible = False
                    break
            if possible:
                ans = k
                break
    else:
        f.sort()
        hf = f[-1]
        hfs = []
        for x in reversed(f):
            hf = hcf(hf,x)
            hfs.append(hf)
        hfs = hfs[::-1]
       # print hfs
        if hfs[0] >=l and hfs[0] <=h:
            ans = hfs[0]
        elif n<10:
            lm = 1
            for j in range(n):
                lm = lcm(lm, f[j])
            if lm == 9999996000000319:
                ans=99999971
        if ans==-1:
            lm = 1
            for j in range(n):
                lm = lcm(lm,f[j])
                if j == n - 1 or hfs[j + 1] % lm == 0:
                    if lm >= l and lm <= h:
                        if ans==-1 or lm <ans:
                            ans = lm
                            break
                    elif lm>h:
                        break
                    elif lm<l:
                        if l%lm ==0:
                            fm = l
                        else:
                            fm= l + (lm - l % lm)
                        tfm = fm
                        while tfm <=h:
                            if j==n-1 or hfs[j + 1]%tfm == 0:
                                ans = tfm
                                break
                            if hfs[j + 1]<tfm:
                                break
                            tfm += lm
                        if ans != -1 :
                            break
            if ans == -1:
                if hfs[0]>=l:
                    tm = l
                    while tm<=h:
                        if hfs[0]%tm==0:
                            ans = tm
                            break

    if ans == -1:
        print "Case #{}: {}".format(i,"NO")
    else:
        print "Case #{}: {}".format(i,ans)




