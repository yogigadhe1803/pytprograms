#create a lambda to calculate products of elements of a sequence

tpl =(2,3,5,-10,16,18)

from functools import reduce
result = reduce(lambda x,y: x*y,tpl)
print(result)
