class Student:
    def __init__(self):
        self.id =100

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

s = Student()
print('Student id = ',s.getId())

s.setId(200)
print('Student id =',s.getId())