def binary(ll):
    return [bin(x)[2:] for x in ll]
def count_one(n):
    return (bin(n)[2:]).count('1')
#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,l = [int(s) for s in raw_input().split(" ")]
    ff = [int(s,2) for s in raw_input().split(" ")]
    rf = [int(s,2) for s in raw_input().split(" ")]
    #print binary(rf)
    score = -1
    for j in range(0,2**(l+1)):
        mff = [x^j for x in ff]
        if sorted(mff) == sorted(rf):
            score = j

            break

    #print binary(ff)

    if score!=-1:
        print "Case #{}: {}".format(i,count_one(score))
    else:
        print "Case #{}: NOT POSSIBLE".format(i)




