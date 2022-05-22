#do list comprehension to display square on integer from 1 to10

lst = []
for i in range(1,11):
    lst.append(i*i)

print(lst)

# the following is equivalent to lst comprehension

lst = [i*i for i in range(1,11)]
print(lst)