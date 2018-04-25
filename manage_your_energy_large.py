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
    vj = [(j,v[j]) for j in range(n)]
    es = [-1 for j in range(n)]
    vj.sort(key=lambda x: x[1])
    vj = vj[::-1]
   # print vj
    for (j,ee) in vj:
        leftj = -1
        rightj  = -1
        for k in reversed(range(j)):
            if es[k] != -1:
                leftj = k
                break
        for k in range(j+1,n):
            if es[k] != -1:
                rightj = k
                break
        if leftj == -1 and rightj == -1:
           # print "center "+str(j)
            es[j] = e
        elif rightj == -1:
          #  print "left"+str(j)
            if (j-leftj)*r >= e:
               es[j] = e
            else:
                es[j] = (j-leftj)*r
        elif leftj == -1:
          #  print "right"+str(j)
            if (rightj-j) * r >= e:
                es[j] = e
            else:
                es[j] = (rightj-j) * r
        else:
           # print "middle"+str(j)
            if (j-leftj)*r >= e and (rightj-j) * r >= e:
                es[j] = e
            elif (j-leftj)*r >= e:
               # print "problem 1"
                es[j] = (rightj-j) * r
            elif (rightj-j) * r >= e:
              #  print "problem 2"
                es[j] = (j - leftj) * r
            else:
              #  print "problem 3"
                step1 = (rightj-j) * r
                step2 = (j - leftj) * r
            #    print step1, step2

                es[j] = step1+step2 - e
                if es[j] < 0 :
                    es[j] = 0
           # print es

    ans = 0
    for j in range(n):
        ans += es[j] * v[j]
  #  print es
    print "Case #{}: {}".format(i,ans)
    sys.stdout.flush()




