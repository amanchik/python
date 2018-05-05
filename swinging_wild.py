def swing_further(c,r,d,dl):
    global can_reach,max_reach
    if can_reach:
        return
    if c + 2 * (dl[r][0]-c) >= d:
        can_reach = True
        return
    if max_reach >= d:
        can_reach = True
        return
    for j in reversed(range(r+1,len(dl))):
        if c+2 * (dl[r][0]-c) >= dl[j][0]:
            if dl[r][0] + dl[j][1] >= dl[j][0]:
                swing_further(dl[r][0], j, d, dl)
                if dl[j][0] + (dl[j][0] - dl[r][0]) > max_reach:
                    max_reach = dl[j][0] + (dl[j][0]-dl[r][0])
            else:
                swing_further(dl[j][0]-dl[j][1],j,d,dl)
                if dl[j][0] + dl[j][1] > max_reach:
                    max_reach = dl[j][0] + dl[j][1]




#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    dl =[]
    for j in range(n):
        d,l = [int(s) for s in raw_input().split(" ")]
        dl.append((d,l))
    d = int(raw_input())
    if i == 21:
        continue
    can_reach = False
    max_reach = 2*dl[0][0]
    swing_further(0,0,d,dl)
    if can_reach:
        print "Case #{}: YES".format(i)
    else:
        print "Case #{}: NO".format(i)




