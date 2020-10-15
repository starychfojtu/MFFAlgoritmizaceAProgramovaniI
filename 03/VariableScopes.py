a = 2
b = 3

def foo(b):
  a = b + 1 # local a = 3 + 1 = 4
  a = a + 1 # local a = local a + 1 = 5
  return a # 5

def bar():
  global b
  b = a + 3 # global b = global a + 3 = 5
  return b # global b = 5

def baz():
  return a + b # global a + global b = 7

def thud():
  a = b + 1 # Error: reading before assignment of b
  b = a + 1
  return a

print(foo()) # 5
print(bar()) # 5
print(baz()) # 7
print(thud())