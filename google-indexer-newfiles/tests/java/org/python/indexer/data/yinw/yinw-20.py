def f():
  def g1(x):
    return g2(x)
  def g2(y):
    return y+z
  z = 3
  print g1(1)

f()
