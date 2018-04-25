def loser(c):
    if c == 'P':
        return 'R'
    elif c=='S':
        return 'P'
    else:
        return 'S'
def glue_alpha(s1,s2):
    if s1 < s2:
        return s1+s2
    else:
        return s2+s1
def get_next(s):
    if len(s) == 2:
        first = glue_alpha(s[0],loser(s[0]))
        second = glue_alpha(s[1],loser(s[1]))
        return glue_alpha(first,second)
    else:
        first = get_next(s[0:len(s)/2])
        second = get_next(s[len(s)/2:])
        return glue_alpha(first,second)
rounds = [[] for j in range(13)]
first_round = ['PR','PS','RS']
rounds[1] = first_round
for j in range(2,13):
        next_round = []
        for x in first_round:
            next_round.append(get_next(x))
        rounds[j] = next_round
        first_round = next_round

t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n,r,p,s = [int(s) for s in raw_input().split(" ")]
    printed_output = False
    for x in rounds[n]:
        r1 = x.count('R')
        p1 = x.count('P')
        s1 = x.count('S')
        if r == r1 and p == p1 and s==s1:
            print "Case #{}: {}".format(i, x)
            printed_output = True
            break
    if not printed_output:
        print "Case #{}: {}".format(i, 'IMPOSSIBLE')



