#write a funct that returns result of addition and subtraction of 2 nos

def add_sub(a,b):
    x = a+b
    y = a-b
    return x,y

a,b = add_sub(10,20)
print('result of add = ',a)
print('result of sub =',b) 
