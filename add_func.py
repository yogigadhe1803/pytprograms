def add(a,b):
    g = a+b
    return g

def facto(a,b):
    result = 1
    g = add(a,b)
    while g > 0:
        result = result * g
        g = g -1
    print('factorial of {} is {}.'.format(add(a,b),result))

fact(10,5)
