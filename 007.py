# project euler: problem 7 (http://projecteuler.net/problem=7)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

from modules.primes import primes

print list(primes(120000))[10001]

# answer: 104759
# runtime: 0.1s