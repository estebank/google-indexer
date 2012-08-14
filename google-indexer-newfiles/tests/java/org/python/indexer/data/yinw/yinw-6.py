def ok():
    x = 1
    class A:
        x = 2
        def f(self,y):
            x = 3
            print x,y
        def g(me):
            print me.x
            print me
            print x
            print im_self
            print __class__
    o = A()
    o.g()


# locations:
# 	<Name:x:7:18> = [<Name:x:6:12>]
# 	<Name:me:9:18> = [<ClassDef:A:3:4>]
# 	<Attribute:<Name:me:9:18>.x:9:18> = [<Name:x:4:8>]
# 	<Name:x:10:18> = [<Name:x:2:4>]
# 	<Name:A:11:8> = [<ClassDef:A:3:4>]
# 	<Name:o:12:4> = [<Name:o:11:4>]
# 	<Attribute:<Name:o:12:4>.g:12:4> = [<Function:g:8:8>]
