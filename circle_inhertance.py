class square:
    def __init__(self,x):
        self.x =x

    def area(self):
        print('area of square is :',self.x*self.x)

class circle(square):
    def __init__(self,x):
        super().__init__(x)
 
    def area(self):
        super().area()
        print('Area of circle is:',self.x*self.x*22/7)

a = circle(10)
a.area()