def g(x):
  return x + 1

def f(x, y=g(3), *kw):
  return x, y, kw
