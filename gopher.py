import sys
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
  a = int(raw_input())
  w, h = 1000,1000
  grid = [[0 for x in range(w)] for y in range(h)]
  x = 2
  y = 2
  finished = False
  while not finished:
      print x,y
      sys.stdout.flush()
      n, m = [int(s) for s in raw_input().split(" ")]
      sys.stderr.write(str(n)+" "+str(m))
      if n==0 and m == 0 :
          finished = True
          break
      if n == -1 and m == -1 :
          finished = True
          break
      grid[n-1][m-1] = 1
      three = True
      for j in range(3):
          for k in range(3):
              if grid[x+j-2][y+k-2] == 0 :
                  three = False
                  break
      if three:
          y += 3
          if y == 999 :
              x += 2
              y = 2




