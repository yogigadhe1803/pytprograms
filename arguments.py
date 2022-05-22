#positional arguments = passed in the correct order

def join(a,b):
    c = a+b
    print(c)

join('Auranga' , 'bad')

#keyword arguments -> passed by the parameter name


def join(a,b):
    c = a+b
    print(c)

join(a='Auranga', b='bad') #keyword

join(b='bad',a='Auranga')



#default arguments -> that uses default value

def grocery(item,price=50.00): #->here price=50.00 is default argument
    print('Item name= ', item)
    print("Price= %.2f" % price)

grocery('Sugar')


#variable length arguments-> tht can store 0 or more values

def add(n, *x):
    total = n+sum(x)
    print('Total= ',total)

add(10,11,66)
