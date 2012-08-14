class A:
    a = 1

class B:
    a = 2

def g(x):
    print x.a

def h(x):
    print x.a

def gen(u):
    if (u>10): return g
    elif (u>5): return 1
    else: return h
    
ff = gen(2)

# o1 = A()
# o2 = B()

# ff(o1)
# ff(o2)

def k(t):
    if (t>1): return A()
    else: return B()

ff(k(2))
