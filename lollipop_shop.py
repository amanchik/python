import sys
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    j = 0
    can_sell = [k+1 for k in range(n)]
    sold = []
    choices = [int(s) for s in raw_input().split(" ")]
    if choices[0] == -1:
        break

    choices = choices[1:]
    if j==n:
        print -1
    else:
        if can_sell[j] in choices:
            print can_sell[j]
            sold.append(can_sell[j])
    sys.stdout.flush()





