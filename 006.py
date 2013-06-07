# project euler: problem 6 (http://projecteuler.net/problem=6)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

print sum(range(1, 101)) ** 2 - sum([x ** 2 for x in range(1, 101)])

# answer: 25164150
# runtime: 0.1s