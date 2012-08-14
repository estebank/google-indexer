class A:
    a = 1

class B:
    a = 2

def g(x):
    print x.a

o1 = A()
o2 = B()

g(o1)
g(o2)

