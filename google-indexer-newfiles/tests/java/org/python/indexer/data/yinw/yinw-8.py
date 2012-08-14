class A:
    a = 1

class B:
    a = 2

def f(o):
    print o.a()

o1 = A()
o2 = B()
f(o1)
f(o2)


# locations:
# 	<Name:o:8:10> = [<Name:o:7:6>]
# 	<Name:A:10:5> = [<ClassDef:A:1:0>]
# 	<Name:B:11:5> = [<ClassDef:B:4:0>]
# 	<Name:f:12:0> = [<Function:f:7:0>]
# 	<Name:o1:12:2> = [<Name:o1:10:0>]
# 	<Name:f:13:0> = [<Function:f:7:0>]
# 	<Name:o2:13:2> = [<Name:o2:11:0>]
# unbound variables:

# semantic problems:
# unknown variables:
# 	<Attribute:<Name:o:8:10>.a:8:10> = accessing attr of unknown type/unbound variable
# parsing problems:

