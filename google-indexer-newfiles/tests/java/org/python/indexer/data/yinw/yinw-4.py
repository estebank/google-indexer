class A:
    a = 1

class B:
    a = 2
    
o1 = (A(), A(), B())
o2 = o1[1:2]

for x in o2:
    print x.a


# locations:
# 	<Name:A:7:6> = [<ClassDef:A:1:0>]
# 	<Name:A:7:11> = [<ClassDef:A:1:0>]
# 	<Name:B:7:16> = [<ClassDef:B:4:0>]
# 	<Name:o1:8:5> = [<Name:o1:7:0>]
# 	<Name:o2:10:9> = [<Name:o2:8:0>]
# 	<Name:x:11:10> = [<Name:x:10:4>]
# 	<Attribute:<Name:x:11:10>.a:11:10> = [<Name:a:2:4>, <Name:a:5:4>]
