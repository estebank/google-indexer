class A:
    a = 1

def f(x):
    if (x>1): return f(x-1)
    else: return A()

print f(2).a


# test of recursive functions

# locations:
# 	<Name:x:5:8> = [<Name:x:4:6>]
# 	<Name:f:5:21> = [<Function:f:4:0>]
# 	<Name:x:5:23> = [<Name:x:4:6>]
# 	<Name:A:6:17> = [<ClassDef:A:1:0>]
# 	<Name:f:8:6> = [<Function:f:4:0>]
# 	<Attribute:<Call:<Name:f:8:6>:[<Num:2>]:8:6>.a:8:6> = [<Name:a:2:4>]
