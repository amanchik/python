# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
from decimal import *
getcontext().prec = 100
t = int(raw_input()) # read a line with a single integer


def mod(a,b):
    if a > b:
        return a - b
    else:
        return b - a


for i in xrange(1, t + 1):
  a = Decimal(raw_input())
  x = 0
  y = 0
  z = 0
  if a * a <= 2.0000000000000004:
      sin_square = (a*Decimal(mod(2,a*a)).sqrt() + 1)/2
      cos_square = 1-sin_square
      sin = Decimal(sin_square).sqrt()
      cos = Decimal(cos_square).sqrt()

      print "Case #{}:".format(i)
    #  print "{} {} {}".format(sin/2,0, -1*cos/2)
    #  print "{} {} {}".format(cos/2, 0, -1*sin/2)
    #  print "{} {} {}".format(0, -0.5, 0)
      print "{} {} {}".format(sin / 2, cos / 2, 0)
      print "{} {} {}".format(-cos / 2, sin / 2, 0)
      print "{} {} {}".format(0, 0, 0.5)
  else:
      sin = (a + Decimal(mod(6,2*a*a)).sqrt())/2
      cos = Decimal(mod(1, sin * sin)).sqrt()
      root_two = Decimal(2).sqrt()
      print "Case #{}:".format(i)
      print "{} {} {}".format(cos - sin/root_two, 0, cos - sin/root_two)
      print "{} {} {}".format((cos - sin/root_two)/2, Decimal(0.5)/root_two, (cos - sin/root_two)/2)
      print "{} {} {}".format((cos - sin/root_two)/2, Decimal(-0.5)/root_two, (cos - sin/root_two)/2)


  # check out .format's specification for more formatting options
