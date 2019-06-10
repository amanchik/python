def is_valid(s):
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            return False
    return True
def is_valid_max(s):
    discord = 0
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            discord = i
            break
    while int(s[discord]) == int(s[discord-1]):
        discord -= 1
    return  discord
def get_min(s):
    return s[0]*len(s)
def get_previous(s):
    if int(s[0]) == 1:
        return '9'*(len(s)-1)
    else:
        return str(int(s[0])-1)+('9' * (len(s) - 1))
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()
    if is_valid(s):
        print "Case #{}: {}".format(i, s)
    else:
        for p in range(0,len(s)):
            if int(s[p:]) < int(get_min(s[p:])):
                ans = s[0:p] + get_previous(s[p:])
                print "Case #{}: {}".format(i, ans)
                break


