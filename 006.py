# project euler: problem 6 (http://projecteuler.net/problem=6)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

import math

print int(math.pow(reduce(lambda x, y: x + y, range(1, 101), 0), 2) - reduce(lambda x, y: x + math.pow(y, 2), range(1, 101), 0))

# answer: 25164150
# runtime: 0.1s