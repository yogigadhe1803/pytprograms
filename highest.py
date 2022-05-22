#3 numbers are give find the biggest number among them

lst = [int(i) for i in input('Enter three nos : ').split(',')]
lst.sort(reverse=True)

print(lst[0])
