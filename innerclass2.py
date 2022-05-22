class Manager:
    def __init__(self):
        self.id = 10
        self.deptname = 'Administration'
        self.salary = 45000

    def display(self):
        print('manager id = ',self.id)
        print('Department name =',self.deptname)

    class Fullname:
        def __init__(self):
            self.fname = 'Yogesh'
            self.mname = 'Sahdev'
            self.lname = 'Gadhe'

        def display(self):
            print('Full name = {} {} {}' .format(self.fname, self.mname,self.lname))

#m =Manager()
#m.display()
Manager().display()
#n = Manager().Fullname()
#n.display()

Manager().Fullname().display()