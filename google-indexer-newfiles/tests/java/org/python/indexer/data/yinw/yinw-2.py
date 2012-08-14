class A:
    a = 1

class B:
    a = 2
    
l = [A(), A(), B()]

print l[0].a

# locations:
# 	<Name:A:7:5> = [<ClassDef:A:1:0>]
# 	<Name:A:7:10> = [<ClassDef:A:1:0>]
# 	<Name:B:7:15> = [<ClassDef:B:4:0>]
# 	<Name:l:9:6> = [<Name:l:7:0>]
# 	<Attribute:<Subscript:<Name:l:9:6>:<Index:<Num:3>>>.a:9:6> = [<Name:a:5:4>, <Name:a:2:4>]

