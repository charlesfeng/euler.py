# project euler: problem 9 (http://projecteuler.net/problem=9)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

def f():
  for a in range(1, 999):
    for b in range(a, 1000 - a):
      c = 1000 - a - b
      if a * a + b * b == c * c:
        return a * b * c
        
print f()

# answer: 31875000
# runtime: 0.1s