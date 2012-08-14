class A:
    a = 1

class B:
    a = 2

l = [A(), A(), B()]

for x in l:
    print x.a


# locations:
# 	<Name:A:7:5> = [<ClassDef:A:1:0>]
# 	<Name:A:7:10> = [<ClassDef:A:1:0>]
# 	<Name:B:7:15> = [<ClassDef:B:4:0>]
# 	<Name:l:9:9> = [<Name:l:7:0>]
# 	<Name:x:10:10> = [<Name:x:9:4>]
# 	<Attribute:<Name:x:10:10>.a:10:10> = [<Name:a:5:4>, <Name:a:2:4>]
