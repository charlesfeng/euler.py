# project euler: problem 4 (http://projecteuler.net/problem=4)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

import math

def f():
  for i in range(1998, 199, -1):
    for j in range(int(math.ceil(i / 2)), 1000):
      p = (i - j) * j
      
      if str(p)[::-1] == str(p):
        return p
        
print f()

# answer: 906609
# runtime: 0.1s