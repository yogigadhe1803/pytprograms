#crceate a lamba that returns even numbers from the list of numbers

mylst =[2,3,5,6,-7,13,4,16,0,-10]

#syntax  for filter --> filter(lambda, mylst) i.e

obj = filter(lambda x: x%2==0 and x!=0,mylst)
print(list(obj))
