# project euler: problem 5 (http://projecteuler.net/problem=5)

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

m = []

for i in range(2, 21):
  t = i
  
  for j in m:
    t /= 1 if t % j else j
  
  if t != 1:
    m.append(t)
    
print reduce(lambda p, c: p * c, m, 1)

# answer: 232792560
# runtime: 0.1s