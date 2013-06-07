# divisors module

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

def divisors(n, ps = False):
  a = dict()
  
  if ps:
    i, p = 0, ps[0]
    
    while p < n:
      if n % p:
        i, p = i + 1, ps[i + 1]
      else:
        a[p] = a[p] + 1 if p in a else 1
        n, i, p = n / p, 0, ps[0]
    
    if p > 1:
      a[p] = a[p] + 1 if p in a else 1
  
  else:
    p = 2

    while p < n:
      if n % p:
        p += 1
      else:
        a[p] = a[p] + 1 if p in a else 1
        n, p = n / p, 2

    if p > 1:
      a[p] = a[p] + 1 if p in a else 1
  
  return a