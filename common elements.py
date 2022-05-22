a = [10,12,20,-100,99,55]

b = [-100,0,10,22,99,65]

c = []

for i in range(len(a)):
    for x in range(len(b)):
        if (a[i] == b[x]):
            c.append(a[i])
print(c)


#another way

for i in a:
    if i in b:
        c.append(i)
print(c)


#equivalent to list comphere

c = [i for i in a if i in b]
print(c)