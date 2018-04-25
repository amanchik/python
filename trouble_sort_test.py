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
#t = int(raw_input()) # read a line with a single integer
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
def get_index(all_ints):
    right_sort = [s for s in all_ints]
    right_sort.sort()
    troubled = trouble_sort(all_ints)
    ans  = -1
    for j in range(len(all_ints)):
      if troubled[j] != right_sort[j]:
          ans = j
          break
    return ans

tracks = permutations(range(1,5))
all_ans = []
for track in tracks:
   # print track
    ans = get_index(list(track))
    if ans != -1  :
        print trouble_sort(list(track))
        print ans




