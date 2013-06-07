# list product module

# (c) 2013 charles feng (https://github.com/charlesfeng)
# shared under the mit license (http://www.opensource.org/licenses/mit)

def prod(l):
  return reduce(lambda x, y: x * y, l, 1)