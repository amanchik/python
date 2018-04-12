t = int(raw_input()) # read a line with a single integer
def damage(s):
    ans = 0
    strength = 1
    for i in range(0,len(s)):
        if s[i] == 'C':
            strength = strength * 2
        else:
            ans += strength
    return ans


def shuffle_index(s):
    for i in reversed(range(1, len(s))):
        if s[i] == 'S' and s[i-1] == 'C' :
            return i - 1
    return  -1


for i in xrange(1, t + 1):
  n, m = [s for s in raw_input().split(" ")] # read a list of integers, 2 in this case
  n = int(n)
  m  = list(m)
  ans = 0
  possible = True
  while damage(m) > n :
      j = shuffle_index(m)
      if j == -1:
          possible = False
          break
      m[j] = 'S'
      m[j+1] = 'C'
      ans = ans + 1
  if possible:
      print "Case #{}: {}".format(i, ans)
  else:
      print "Case #{}: IMPOSSIBLE".format(i)



