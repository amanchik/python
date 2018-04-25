def digits(n):
    if n>0:
        return 1+digits(n/10)
    else:
        return 0
def reverse_n(n):
    ans = 0
    while n>0:
        ans += (n%10)
        n = n/10
        if n>0:
            ans = ans * 10
    return ans
def previous_dip(n):
    if n<21:
        return n-1
    dg = digits(n)
    half = dg/2
    if dg%2!=0:
        half = half + 1
    tenp = 10**half
    if n%tenp == 0:
        return previous_dip(n-1)
    else:
        poss = ((n/tenp)*tenp) + 1
        rposs = reverse_n(poss)
        if rposs < poss:
            return poss
        else:
            return previous_dip(poss-1)
def counter_value(n):
    if n<21:
        return n
    else:
        pd = previous_dip(n)
        return n-pd+1+counter_value(reverse_n(pd))


t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i,counter_value(n))





