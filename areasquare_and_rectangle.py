class square:
    def __init__(self,x):
        self.x = x

    def area(self):
        print('Area of square is :',self.x*self.x)

class Reactangle(square):
    def __init__(self,x , y):
        super().__init__(x)
        self.y = y
    def area(self):
       # super().area()
        print('Area of rectangle is: ',self.x * self.y)



a = square(10)

a.area()
r = Reactangle(20, 15.5)
r.area()