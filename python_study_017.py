#-*-coding:utf8-*-
class Person(object):
    __count= 0
    def __init__(self,name):
        Person.__count= Person.__count +1
        self.name = name
        print Person.__count
p1 = Person('Bob')
P2 = Person('Alice')

try:

    print Person.__count

except AttributeError:

    print 'attributeerror'