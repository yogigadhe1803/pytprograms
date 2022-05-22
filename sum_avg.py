#write a python program to accept a group of elements and find their
#sum and averager

lst = [float(i) for i in input('Enter nos ; ').split(',')]
s = sum(lst)
a = sum/len(lst)
print('Sum = ', s)
print('Average = ',a)
