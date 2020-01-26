class A:
    property1 = 'prop 1'
    property2 = 'prop 2'
    name = 'geust'

    def say_hi(self, name=''):
        if name:
            return 'Hi, '+ name
        else:
            return 'Hello, ' + self.name

a = A()
b = A()
#
# print(a.property1)
# print(a.property2)
print(a.say_hi('Tim'))
print(b.say_hi('Kitty'))
print(b.say_hi())
