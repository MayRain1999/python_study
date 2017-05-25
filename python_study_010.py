#-*-coding:utf8-*-
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' %(self.name, self.score)

    __repr__ = __str__
#实例化
    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name,s.name)
        return-cmp(self.score, s.score)
L = [Student('Tim',99), Student('Bob', 88), Student('Alice', 99)]

print sorted(L)