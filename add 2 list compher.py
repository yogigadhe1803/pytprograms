# add two list and store the sum of both in c

a = [5, 10, 11, -5, 16, 15]

b = [6, 10, 8, 8, 0, 100]

c = []
for i in range(6):
    c.append(a[i] + b[i])
print(c)


#equivalent to compreh

c= [a[i] + b[i] for i in range(len(a))]
print(c)