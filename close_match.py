import sys
diff = 9999999999999999999
max_di = 9999999999999999999
ac = '1'
ap = '1'
def mod(a,b):
    if a > b:
        return a - b
    else:
        return b - a
def max_diff(ci,pi,c,p,j):
    if int(ci) > int(pi):
        for k in range(len(c)-j):
            ci += '9'
            pi += '0'
        return mod(int(ci),int(pi))
    else:
        for k in range(len(c)-j):
            ci += '0'
            pi += '9'
        return mod(int(ci),int(pi))
def min_diff(ci,pi,c,p,j):
    if int(ci) == int(pi):
        for k in range(len(c)-j):
            ci += '0'
            pi += '0'
        return mod(int(ci), int(pi))
    if int(ci) > int(pi):
        for k in range(len(c)-j):
            ci += '0'
            pi += '9'
        return mod(int(ci),int(pi))
    else:
        for k in range(len(c)-j):
            ci += '9'
            pi += '0'
        return mod(int(ci),int(pi))



def close_match(ci,pi,c,p,j):
    global diff,ac,ap,max_di
   # print max_di,min_diff(ci,pi,c,p,j)
    if min_diff(ci,pi,c,p,j) > max_di:
        return
    elif max_diff(ci,pi,c,p,j)<max_di:
        max_di =  max_diff(ci,pi,c,p,j)
    if j>=len(c):
        if mod(int(ci),int(pi))< diff:
            diff = mod(int(ci),int(pi))
            ac = ci
            ap = pi
        elif mod(int(ci),int(pi)) == diff:
            if int(ci) < int(ac):
                ac = ci
                ap = pi
            elif int(ci) == int(ac) and int(pi) < int(ap):
                ac = ci
                ap = pi
        return
    greater = True
    if int(ci)<int(pi):
        greater = False
    if int(ci)==int(pi):
        if c[j] == '?' and p[j] == '?':
            close_match(ci+'0',pi+'0',c,p,j+1)
            close_match(ci+'1',pi+'0',c,p,j+1)
            close_match(ci+'0',pi+'1',c,p,j+1)
        elif c[j] == '?' and p[j] != '?':
            close_match(ci+p[j],pi+p[j],c,p,j+1)
            if int(p[j]) < 9:
                close_match(ci + str(int(p[j]) + 1), pi + p[j], c, p, j + 1)
            if int(p[j]) > 0:
                close_match(ci + str(int(p[j]) - 1), pi + p[j], c, p, j + 1)
        elif c[j] != '?' and p[j] == '?':
            close_match(ci+c[j],pi+c[j],c,p,j+1)
            if int(c[j]) < 9:
                close_match(ci + c[j], pi + str(int(c[j]) + 1), c, p, j + 1)
            if int(c[j]) > 0:
                close_match(ci + c[j], pi + str(int(c[j]) - 1), c, p, j + 1)
        else:
            close_match(ci+c[j],pi+p[j],c,p,j+1)
    else:
        if c[j] == '?' and p[j] == '?':
            if greater:
                close_match(ci + '0', pi + '9', c, p, j + 1)
            else:
                close_match(ci + '9', pi + '0', c, p, j + 1)
        elif c[j] != '?' and p[j] != '?':
            close_match(ci + c[j], pi + p[j], c, p, j + 1)
        elif c[j] != '?' and p[j] == '?':
            close_match(ci + c[j], pi + c[j], c, p, j + 1)
            if greater:
                close_match(ci + c[j], pi + '9', c, p, j + 1)
            else:
                close_match(ci + c[j], pi + '0', c, p, j + 1)
            if int(c[j]) < 9:
                close_match(ci + c[j], pi + str(int(c[j])+1), c, p, j + 1)
            if int(c[j]) > 0:
                close_match(ci + c[j], pi + str(int(c[j])-1), c, p, j + 1)
        elif c[j] == '?' and p[j] != '?':
            close_match(ci + p[j], pi + p[j], c, p, j + 1)
            if greater:
                close_match(ci + '0', pi + p[j], c, p, j + 1)
            else:
                close_match(ci + '9', pi + p[j], c, p, j + 1)
            if int(p[j]) < 9:
                close_match(ci + str(int(p[j]) + 1), pi +p[j] , c, p, j + 1)
            if int(p[j]) > 0:
                close_match(ci + str(int(p[j]) - 1), pi +p[j] , c, p, j + 1)


#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    c,p = [list(s) for s in raw_input().split(" ")]
    diff = 9999999999999999999
    max_di = 9999999999999999999

    if c[0] == '?' and p[0] == '?':
        close_match('0','0',c,p,1)
        close_match('1','0',c,p,1)
        close_match('0','1',c,p,1)
    elif c[0]!='?' and p[0]!='?':
        close_match(c[0],p[0],c,p,1)
    elif c[0]!='?' and p[0] == '?':
        close_match(c[0], c[0], c, p, 1)
        if int(c[0]) < 9:
            close_match(c[0], str(int(c[0]) + 1), c, p,  1)
        if int(c[0]) > 0:
            close_match(c[0], str(int(c[0]) - 1), c, p,  1)
    elif c[0]=='?' and p[0] != '?':
        close_match(p[0], p[0], c, p, 1)
        if int(p[0]) < 9:
            close_match(str(int(p[0]) + 1),p[0], c, p, 1)
        if int(p[0]) > 0:
            close_match(str(int(p[0]) - 1),p[0], c, p, 1)
    print "Case #{}: {} {}".format(i,ac,ap)
    #print diff
    sys.stdout.flush()







