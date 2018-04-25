def binary(ll):
    return [bin(x)[2:] for x in ll]
#print pi
def find_score(ff,rf,j,score,l):
    if sorted(ff) == sorted(rf):
        return score
    two = 2 ** j
    mff = sorted([x % two for x in ff])
    mrf = sorted([x % two for x in rf])

    mmff = sorted([(x ^ (two / 2)) % two for x in ff])
    if mff != mrf and mmff != mrf:
        return  -1
    if mrf == mrf and mmff == mrf:
        dff = [x ^ (two / 2) for x in ff]
        score1 = find_score(ff,rf,j+1,score,l)
        score2 = find_score(dff,rf,j+1,score+1,l)
        if score1 == -1 and score2 == -1:
            return  -1
        if score1 == -1:
            return  score2
        if score2 == -1:
            return  score1
        if score1<score2:
            return score1
        else:
            return score2
    elif mrf == mrf:
        return find_score(ff,rf,j+1,score,l)
    else:
        dff = [x ^ (two / 2) for x in ff]
        return  find_score(dff,rf,j+1,score+1,l)





t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,l = [int(s) for s in raw_input().split(" ")]
    ff = [int(s,2) for s in raw_input().split(" ")]
    rf = [int(s,2) for s in raw_input().split(" ")]
    #print binary(rf)
    score = find_score(ff,rf,1,0,l)

    if score!=-1:
        print "Case #{}: {}".format(i,score)
    else:
        print "Case #{}: NOT POSSIBLE".format(i)




