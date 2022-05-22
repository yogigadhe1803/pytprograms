#TO find factorial og given nos

def fact(n):
    if n==0:
        res = 1
    else:
        res = n*fact(n-1)
    return res

r = fact(15)
print('Factorial value= ',r)

'''
for i in range(1,11):
    print('Factorial value of {} is {}'.format(i, fact(i)))
'''
