class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k , v in kw.iteritems():
            setattr(self,k,v)
p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course