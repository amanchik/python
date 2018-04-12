t = int(raw_input()) # read a line with a single integer
def trouble_sort(L):
    done = False
    while not done:
        done = True
        for i in range(0,len(L)-2):
            if L[i] > L[i+2]:
                done = False
                save = L[i]
                L[i] = L[i+2]
                L[i+2] = save
    return  L


for i in xrange(1, t + 1):
  n = raw_input()
  all_ints = [int(s) for s in raw_input().split(" ")] # read a list of integers, 2 in this case
  right_sort = [s for s in all_ints]
  right_sort.sort()
  troubled  = trouble_sort(all_ints)
  #print(right_sort)
  #print(trouble_sort(all_ints))
  ans  = -1
  for j in range(len(all_ints)):
      if troubled[j] != right_sort[j]:
          ans = j
          break
  if ans == -1 :
      print "Case #{}: OK".format(i)
  else:
      print "Case #{}: {}".format(i,ans)

