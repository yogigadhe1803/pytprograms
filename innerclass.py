'''
class Student:
    def __init__(self):
        self.rno = 11
        self.name = 'yogesh'

    def display(self):
        print('rno= ', self.rno)
        print('name= ',self.name)

    class dob:
        def __init__(self):
            self.dd = 15

            self.mm = 3
            self.yy = 1997

        def display(self):
            print('date of birth= {}/{}/{}'.format(self.dd,self.mm,self.yy))


st = Student()
st.display()
d = Student().dob()
d.display()

'''

class Student:
    def __init__(self):
        self.rno = 11
        self.name = 'yogesh'

    def display(self):
        print('Roll no of student is',self.name)
        print('Name of student is ',self.rno)

    class DOB:
        def __init__(self):
            self.dd = 18
            self.mm = 3
            self.yy = 2000

        def display(self):
            print('Date of birth = {}/{}/{}'.format(self.dd,self.mm,self.yy))

st = Student()
st.display()

d = st.DOB()
d.display()