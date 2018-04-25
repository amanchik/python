import sys
start = [2,3,4,5]
for j in range(2,1000000):
    prime = True
    for x in start:
        if j%x==0 :
            prime = False
            break
        if x*x > j:
            break

    if prime and j>start[-1]:
        start.append(j)
        sys.stdout.flush()
n = 99999971
for x in start:
    if n%x==0:
        print x