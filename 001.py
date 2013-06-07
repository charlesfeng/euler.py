n = 0

for i in range(0, 1000):
  n += 0 if i % 3 and i % 5 else i
  
print n