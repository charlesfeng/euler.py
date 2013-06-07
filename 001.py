# project euler: problem 1 (http://projecteuler.net/problem=1)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

n = 0

for i in range(0, 1000):
  n += 0 if i % 3 and i % 5 else i
  
print n