# project euler: problem 12 (http://projecteuler.net/problem=12)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

import math

def primes(l):
  a = [False, False] + [True] * (l - 2)

  for (i, p) in enumerate(a):
    if p:
      yield i
      a[i * i : l : i] = [False] * int(math.ceil(float(l - i * i) / i))

def prod(l):
  return reduce(lambda x, y: x * y, l, 1)

def nd(n, ps):
  a = dict()
  i, p = 0, ps[0]
  
  while p < n:
    if n % p:
      i, p = i + 1, ps[i + 1]
    else:
      a[p] = a[p] + 1 if p in a else 1
      n, i, p = n / p, 0, ps[0]
  
  if p > 1:
    a[p] = a[p] + 1 if p in a else 1
  
  return prod([x + 1 for x in a.itervalues()])

ps = list(primes(10000000))

d = n = 6

while d < 500:
  n += 1
  d = nd(n * (n + 1) / 2, ps)

print n * (n + 1) / 2

# answer: 76576500
# runtime: 4.9s