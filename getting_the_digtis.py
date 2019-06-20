digits =["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
all_digits = ''.join(digits)
all_digits = list(all_digits)
all_digits = set(all_digits)
# print all_digits
counts = {}
for x in digits:
    counts[x]={}
    for c in all_digits:
        counts[x][c]=x.count(c)
#print counts

#print ans
def reduce_vector(v,p):
  #  assert len(v) == len(p)
    return [a  for a, b in zip(v, p) if b!=0]
def decrease_vector(v, knowns):
    return  [v[j] if digits[j] not in knowns else 0 for j in range(10) ]
# ans = zip(*ans) # transpose the matrix
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    ans = []
    for c in all_digits:
        tmp = []
        for x in digits:
            tmp.append(counts[x][c])
        ans.append(tmp)
    knowns = {}
    unknowns = []
    s = raw_input()
    tmp = []
    for c in all_digits:
        count = s.count(c)
        tmp.append(count)
        if count == 0:
            for digit in digits:
                if counts[digit][c] != 0:
                    knowns[digit] = 0


    possible = True
    while possible:
        possible = False
        for j in range(len(ans)):
            for k in range(len(ans[j])):
                if digits[k] in knowns and ans[j][k] != 0:
                    possible = True
         #           print digits[k],knowns[digits[k]],ans[j],tmp[j]
                    tmp[j] -= ans[j][k] * knowns[digits[k]]
                    ans[j][k] = 0
        for j in range(len(ans)):
            if sum(ans[j]) == 1:
                possible = True
        #        print ans[j]
                index = ans[j].index(1)
                knowns[digits[index]] = tmp[j]
   # print ans
   # print tmp
   # print knowns

    ls = ''
    for k in range(10):
        if knowns[digits[k]] != 0 :
            ls += str(k) * knowns[digits[k]]
    print "Case #{}: {}".format(i, ls)


 #   print ans
 #   print tmp

'''

    asolve = []
    bsolve = []
    for j in range(len(tmp)):
        if tmp[j] != 0 :
            asolve.append(decrease_vector(ans[j],knowns))
            bsolve.append(tmp[j])

    print ans
    print tmp
    print asolve
    print bsolve
    ln = len(asolve[0])
    a = np.array(asolve[0:ln])
    b = np.array(bsolve[0:ln])
'''
   # x = np.linalg.solve(a, b)
   # final = [int(k) for k in x]
   # ls = ''
   # for k in range(10):
    #    if final[k] != 0:
    #        ls += str(k)*final[k]
    #print "Case #{}: {}".format(i, ls)