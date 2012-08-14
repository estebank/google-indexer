class A:
    a = 1

class B:
    def baz(self):
        self.a = 1
    def aa(me):
        me.a = 2
    def foo(self):
        return self.a
    def bar(self):
        return self.a
    def __iter__(self):
        return self


o = B()

for x in o:
    print x.a


# locations:
# 	<Name:A:6:17> = [<ClassDef:A:1:0>]
# 	<Name:self:6:8> = [<ClassDef:B:4:0>]
# 	<Name:self:8:15> = [<ClassDef:B:4:0>]
# 	<Attribute:<Name:self:8:15>.b:8:15> = [<Attribute:<Name:self:6:8>.b:6:8>]
# 	<Name:B:10:4> = [<ClassDef:B:4:0>]
# 	<Name:o:12:9> = [<Name:o:10:0>]
# 	<Name:x:13:10> = [<Name:x:12:4>]
# 	<Attribute:<Name:x:13:10>.a:13:10> = [<Name:a:2:4>]
