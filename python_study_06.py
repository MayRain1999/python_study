import  json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'
s = Students()
print json.load(s)