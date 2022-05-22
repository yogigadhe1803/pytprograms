'''class Student:
    #default construstor
    def __init__(self):
        self.name= 'yogesh'
        self.rollno = 10
        self.marks =[65,55,77,88,99]
'''
class Student():
    def __init__(self,rollno,name,marks):
        self.rollno= rollno
        self.name= name
        self.marks = marks


    def display(self):
        print('Rollno =',self.rollno)
        print('Name:',self.name)
        print('Marks : ',self.marks)
        tot = sum(self.marks)
        print('Totalmarks = %d' % tot)
        percentage = tot/len(self.marks)
        print('Percentage= %.2f' % percentage)


s1 = Student(7,'yogesh',[88,95,87,93,92])
s1.display()


'''s1 = Student()
s1.display()'''