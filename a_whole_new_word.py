def next_seq(start,sets):
    index = -1
    for j in reversed(range(len(start))):
        if start[j] < len(sets[j]) - 1:
            index = j
            break
    if index == -1:
        return
    start[index] = start[index] + 1

    for j in range(index+1,len(start)):
            start[j] = 0
def is_last(start,sets):
    for j in range(len(start)):
        if start[j] < len(sets[j]) - 1:
            return False
    return True

#print pi
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n, l = [int(s) for s in raw_input().split(" ")]
    words = []
    for j in range(n):
        words.append(raw_input())
    ans = 1
    sets = []
    for j in range(l):
        letters = [x[j] for x in words]
        ans = ans * len(set(letters))
        sets.append(sorted(list(set(letters))))

    if ans == n:
        print "Case #{}: {}".format(i,'-')
    else:
        words.sort()
        start = [0 for j in range(l)]
        counter = 0
        while True:
            ans = ''.join([sets[j][start[j]] for j in range(l)])
            if ans != words[counter%n]:
                print "Case #{}: {}".format(i, ans)
                break
            counter += 1
            next_seq(start,sets)






