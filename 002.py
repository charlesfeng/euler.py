i = 1
j = 2
n = 0

while i < 4000000:
  n += (0 if i % 2 else i) + (0 if j > 4000000 or j % 2 else j)
  i += j
  j += i
  
print n