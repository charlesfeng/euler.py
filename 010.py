# project euler: problem 10 (http://projecteuler.net/problem=10)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

from modules.primes import primes
  
print sum(list(primes(2000000)))

# answer: 142913828922
# runtime: 0.7s