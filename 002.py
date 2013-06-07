# project euler: problem 2 (http://projecteuler.net/problem=2)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

i, j, n = 1, 2, 0

while i < 4000000:
  n += (0 if i % 2 else i) + (0 if j > 4000000 or j % 2 else j)
  i, j = i + j, i + 2 * j
  
print n

# answer: 4613732
# runtime: 0.1s