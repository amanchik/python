

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    r,c,w = [int(s) for s in raw_input().split(" ")]
    score = r *(c/w)
    score += (w-1)
    if c%w:
        score = score+1
    print "Case #{}: {}".format(i,score)



