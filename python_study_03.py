#-*-coding:utf8-*-
class Person(object):
    __count = 0
    @classmethod
    #定义一个类方法 访问实例属性
    def how_many(cls):
        return cls.__count
    def __init__(self,name):
        self.name = name
        Person.__count = Person.__count + 1
print Person.how_many()
p1 = Person('Bob')
print Person.how_many()