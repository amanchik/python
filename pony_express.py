import sys
def get_min_time(ed,cur,ds,time_so_far,es,matrix,hr,horses):
    global min_time,stack
    if cur == ed:
        if time_so_far < min_time:
            min_time = time_so_far
        return
    if time_so_far > min_time:
        return
    if stack > 45000:
        return
    stack += 1
    for j in range(len(matrix[cur-1])):
        x = matrix[cur-1][j]
        if x != -1:
            if ds + x <= es[hr-1][0] :
                get_min_time(ed,j+1,ds+x,time_so_far + (1.0*x/es[hr-1][1]),es,matrix,hr,horses)
               # print "old"+str(cur)
            if horses[cur-1] and x <= es[cur-1][0]:
                tmp = [k for k in horses]
                tmp[cur-1] = False
               # print  "new "+str(cur)
                get_min_time(ed,j+1,x,time_so_far + (1.0*x/es[cur-1][1]),es,matrix,cur,tmp)





t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,q = [int(s) for s in raw_input().split(" ")]
    es = []
    for j in range(n):
        e,s = [int(s) for s in raw_input().split(" ")]
        es.append((e,s))
    matrix = []
    for _ in range(n):
        mx = [int(s) for s in raw_input().split(" ")]
        matrix.append(mx)
    destinations = []
    for _ in range(q):
        u,v = [int(s) for s in raw_input().split(" ")]
        destinations.append((u,v))
  #  print n,q
  #  print es
    sys.stdout.flush()
    ans = []
    for x in destinations:
        stack = 0
        horses = [True for j in range(n)]
        horses[x[0]-1]=False
        min_time = 9999999999999999
        get_min_time(x[1],x[0],0,0,es,matrix,x[0],horses)
        ans.append("{0:.15f}".format(min_time))
    print "Case #{}: {}".format(i,' '.join(ans))
    sys.stdout.flush()




