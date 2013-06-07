# project euler: problem 12 (http://projecteuler.net/problem=12)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

def prod(l):
  return reduce(lambda x, y: x * y, l, 1)

def nd(n):
  a = dict()
  p = 2
  
  while p < n:
    if n % p:
      p += 1
    else:
      a[p] = a[p] + 1 if p in a else 1
      n, p = n / p, 2
  
  if p > 1:
    a[p] = a[p] + 1 if p in a else 1
  
  return prod([x + 1 for x in a.itervalues()])
  
d = n = 0

while d < 500:
  n += 1
  d = nd(n * (n + 1) / 2)

print n * (n + 1) / 2

# answer: 76576500
# runtime: 7.8s