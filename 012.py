# project euler: problem 12 (http://projecteuler.net/problem=12)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

from modules.prod import prod
from modules.primes import primes
from modules.divisors import divisors

ps = list(primes(10000000))
d = n = 6

while d < 500:
  n += 1
  d = prod([x + 1 for x in divisors(n * (n + 1) / 2, ps).itervalues()])

print n * (n + 1) / 2

# answer: 76576500
# runtime: 4.9s