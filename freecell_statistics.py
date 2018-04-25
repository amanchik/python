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

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,pd,pg = [int(s) for s in raw_input().split(" ")]
    if (pg==100 and pd!=100 ) or (pg==0 and pd!=0):
        print "Case #{}: Broken".format(i)
    else:
        if (pg==100 and pd==100 ) or (pg==0 and pd==0) or pd==0:
            print "Case #{}: Possible".format(i)
        else:
            hf = hcf(100,pd)
            if (100/hf)>n:
                print "Case #{}: Broken".format(i)
            else:
                print "Case #{}: Possible".format(i)






