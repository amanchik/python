def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def flip(n,copy):
    if copy:
        return long(str(n) + str(n)[::-1])
    else:
        return long(str(n) + '1' + str(n)[::-1])


def append_zero(n):
    return long(str(n) + '0' + str(n)[::-1])


def stick_two(n):
    return long(str(n)+'2'+str(n)[::-1])


def generate_binary(t):
    result = ''
    for i in range(0,25):
        if i in t:
            result += '1'
        else:
            result += '0'
    return long(result)


def generate_binary_two(t):
    result = ''
    for i in range(0,25):
        if i in t:
            result += '2'
        else:
            result += '0'
    return long(result)


all_numbers = []


def print_all(x):
    for y in x:
        xx = generate_binary(y)
        all_numbers.append(flip(xx,True))
        all_numbers.append(flip(xx,False))
        all_numbers.append(append_zero(xx))


def add_twos(x):
    for y in x:
        xx = generate_binary(y)
        all_numbers.append(stick_two(xx))


def two_ends(x):
    for y in x:
        xx = generate_binary_two(y)
        all_numbers.append(flip(xx,True))
        all_numbers.append(flip(xx,False))
        all_numbers.append(append_zero(xx))


single = '1' + '0' * 24
double = '11' + '0' * 23
triple = '111' + '0' * 22
quadruple = '1111' + '0' * 21

print_all(combinations(range(25),4))
print_all(combinations(range(25),3))
print_all(combinations(range(25),2))
print_all(combinations(range(25),1))
add_twos(combinations(range(25),2))
add_twos(combinations(range(25),1))
two_ends(combinations(range(25),1))
all_numbers.append(1)
all_numbers.append(2)
all_numbers.append(3)
all_numbers.sort()
squares = [x*x for x in all_numbers]
#print (squares)
#print(len(all_numbers))

T = raw_input("")
T = int(T)
for t in range(1,T+1):
    line = raw_input()
    parts = line.split()
    first = long(parts[0])
    second = long(parts[1])
    ans = 0
    for x in squares:
        if x >= first and x <= second:
            ans += 1
          #  print x
    print "Case #"+str(t)+": "+str(ans)

#print_all(permutations(double))
#print_all(permutations(triple))
#print_all(permutations(quadruple))


