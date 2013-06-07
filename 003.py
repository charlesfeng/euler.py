# project euler: problem 3 (http://projecteuler.net/problem=3)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

n = 600851475143
p = 2
f = 0

while p < n:
  if n % p:
    p += 1
  else:
    f, n, p = (f if f > p else p), n / p, 2

if p > 1:
  f = f if f > p else p

print f

# answer: 6857
# runtime: 0.2s