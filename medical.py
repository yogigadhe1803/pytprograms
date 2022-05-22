m = {1: 'dolo', 2: 'para', 3: 'evil', 4: 'omee'}
d =[int(x) for x in input("Enter the disease : ").split()]
if type(d) != list:
    if d == 1:
        print('dolo 650')
        if d==1:
            print('price= 50')
    elif d == 2:
        print('para')
        if d==2:
            print('price=20')
    elif d==3:
        print('evil')
        if d==3:
            print('price=30')
else:
    if 1 in d: print('dolo 650\tprice = 50')
    if 2 in d: print('para2\tprice = 20')
    if 3 in d: print('evil\tprice = 30')