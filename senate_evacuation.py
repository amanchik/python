t = int(raw_input()) # read a line with a single integer

parties = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in xrange(1, t + 1):
    n = int(raw_input())
    p = [int(s) for s in raw_input().split(" ")]
    total = sum(p)
    tip = [(parties[j],p[j]) for j in range(n)]
    ans = []
    while total > 0:
        tip.sort(key=lambda x: x[1])
      #  print tip
        if (len(tip) >= 3 and (tip[-1][1]-1)*2 <= total-2 and tip[-3][1]*2 <= total-2) or (len(tip)==2 and (tip[-2][1]-1)*2 <= total-2):
            ans.append(tip[-1][0]+tip[-2][0])
            total -= 2
            tip[-2] = (tip[-2][0],tip[-2][1]-1)
            tip[-1] = (tip[-1][0],tip[-1][1]-1)
        else:
            ans.append(tip[-1][0])
            total -= 1
            tip[-1] = (tip[-1][0], tip[-1][1] - 1)
    print "Case #{}: {}".format(i, ' '.join(ans))
