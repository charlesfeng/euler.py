# project euler: problem 7 (http://projecteuler.net/problem=7)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

import math

def primes(l):
  a = [False, False] + [True] * (l - 2)

  for (i, p) in enumerate(a):
    if p:
      yield i
      a[i * i : l : i] = [False] * int(math.ceil(float(l - i * i) / i))

ps = []

for i in primes(120000):
  ps.append(i)

print ps[10001]

# answer: 104759
# runtime: 0.1s