import sys
def countServedCustomers(T,B,bs):
    if T < 0:
        return 0
    served_customers = 0
    for barber in range(B):
        served_customers += ((T/bs[barber]) + 1)
    return served_customers
def naiveGetBarberNumber(n,b,bs):
    max_time = 1000001 * (10**9)
    min_time = -1
    while min_time+1 < max_time:
        mid = (min_time + max_time) / 2
        if countServedCustomers(mid, b, bs) < n:
            min_time = mid
        else:
            max_time = mid
    customers_served_before = countServedCustomers(max_time - 1, b, bs)
    customers_to_be_served = n - customers_served_before
    for j in range(b):
        if (max_time) % bs[j] == 0:
            customers_to_be_served = customers_to_be_served - 1
            if customers_to_be_served == 0:
                return j+1

def hcf(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a%b == 0:
        return b
    elif b%a == 0:
        return a
    elif a>b:
        return hcf(b,a%b)
    else:
        return hcf(a,b%a)
def lcm(a,b):
    return (a*b)/hcf(a,b)
def calc(b,n,bs,mm):
        tops = []
        m = 0
        while True:
            for j in range(b):
                tops.append((m * bs[j], j))
            m = m + 1
            if m > mm:
                break
        stops = sorted(tops, key=lambda element: (element[0], element[1]))
       # print stops
        return stops[n-1][1]+1

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    b,n = [int(s) for s in raw_input().split(" ")]
    bs = [int(s) for s in raw_input().split(" ")]


    print "Case #{}: {}".format(i, naiveGetBarberNumber(n,b,bs))
    sys.stdout.flush()







