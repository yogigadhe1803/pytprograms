class Manager():
    def __init__(self,id,name,add,monsal):
        self.id = id
        self.name = name
        self.add = add
        self.monsal = monsal


    def display(self):
        print('Manager id :',self.id)
        print('Name of Employee: ',self.name)
        print('Adderss :',self.add)
        print('Monthly salary: ',self.monsal)
        anualsal = self.monsal*12
        print('Annual salary :',anualsal)
        tax = anualsal * 0.1
        print('Income tax per annum: ' ,tax)

s1 = Manager(22,'varad','aurangabad',45000)
s1.display()

s2 = Manager(23,'shubham','pune',95000)
s2.display()