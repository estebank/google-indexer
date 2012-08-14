x = 1

def f(y):
  y = x
  x = 3
  print x

def g():
  x = 3
  print x

f(1)
g()
