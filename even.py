# write a list comprehension to get even nos
lst = []
for i in range(2, 11, 2):
    lst.append(i)
print(lst)

#evqivqlent compher

lst = [x for x in range(2 , 11 , 2)]
print(lst)



#2nd way for even no
''''''
lst = []
for i in range(1, 11):
    if i%2==0:
        lst.append(i)
print(lst)

''''''

#equivalent list comphere

lst = [i for i in range(2,11) if i%2==0]
print(lst)
##
