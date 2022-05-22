i = 1
while i <= 50:
    print(i)
    i = i+1

i = 0
while i < 5:
    print('Yogesh')
    i = i + 1

lst = []
for i in range(10):
    lst.append(i)
print(lst)

for i in range(20):
    if i % 2 != 0:
        continue
    print(i)

num = int(input('Enter a number: '))

for i in range(10,0,-1):
    print(f'{num} X {i} = {num*i}')


lst = ['varad', 'shubham', 'saurabh', 'yogesh', 'sachin']
a = 's'
for i in lst:
    if i[0]==a:
        print(i)

num = int(input('Enter a number: '))

i = 0
while i <=10:
    #print(f'{num} x {i} = {num * i}')
    print(str(num) + ' x ' + str(i) + ' = ', num*i )
    i = i + 1

Write a program to find whether a given number is prime or not.

num =int(input('Enter a number: '))
prime = True
for i in range(2,num):
    if num % i == 0:
        prime = False
        break
if prime:
    print('This number is prime')
else:

    print('This number is not prime')

Write a program to calculate the factorial of a given number using for loop.

num = int(input('Enter a number: '))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(f'The factorial of this number is {factorial}')

Write a program to find the sum of first n natural numbers using a while loop.

num = int(input('Enter a number: '))
sum = 0
for i in range(1,num + 1):
    sum = sum + i
print(f'The sum till {num} is {sum}')













