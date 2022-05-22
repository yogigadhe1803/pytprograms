#number is even or not

def even(x):
    
    if x%2==0:
        return 'even'
    else:
        return 'not even'

res = even(5)
print(res)

#lambda

f =(lambda x :'Even' if x%2==0 else 'Not even')
print(f(5))
 
