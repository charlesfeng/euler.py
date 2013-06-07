# project euler: problem 2 (http://projecteuler.net/problem=2)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

i = 1
j = 2
n = 0

while i < 4000000:
  n += (0 if i % 2 else i) + (0 if j > 4000000 or j % 2 else j)
  i += j
  j += i
  
print n