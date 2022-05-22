#retrive first letter of word

words = ['Delhi' , 'Mumbai', 'Pune' , 'Banglore' , 'Hyderabad']

x = []

for i in words:
    x.append(i[0])
print(x)

#equivalent comphere

x = [i[0] for i in words ]
print(x)