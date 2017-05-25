class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course = course
t = Teacher('Alice','Female','English')
print t.name
print t.course