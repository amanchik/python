import sys
max_gain = 0
def energy_max(e,g,ce,r,v,n,j):
    global max_gain
    if j == n:
        if g > max_gain:
            max_gain = g
        return
    '''
    energy_max(e,g+ce*v[j],r,r,v,n,j+1)
    energy_max(e,g+r*v[j],ce,r,v,n,j+1)
    if ce + r <= e :
        energy_max(e,g,ce+r,r,v,n,j+1)
    else:
        energy_max(e,g+(ce+r-e)*v[j],e,r,v,n,j+1)
    '''
    for k in range(0,ce+1):
        if ce-k+r < e:
            energy_max(e, g + k * v[j], ce-k+r, r, v, n, j + 1)
        else:
            energy_max(e, g + k * v[j], e, r, v, n, j + 1)






#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    e,r,n= [int(s) for s in raw_input().split(" ")]
    v= [int(s) for s in raw_input().split(" ")]
    max_gain = 0
    energy_max(e,0,e,r,v,n,0)
    print "Case #{}: {}".format(i,max_gain)
    sys.stdout.flush()




