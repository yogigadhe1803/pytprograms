class Father:
    def height(self):
        print('Height = 6ft')

class Mother:
    def colour(self):
        print('colour of mother = black')

class Child(Father,Mother):
        pass


ch = Child()
ch.height()
ch.colour()