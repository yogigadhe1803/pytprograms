#Write a program using the function to find the greatest of three numbers.

# def maximum(num1,num2,num3):
#     if num1>num2:
#         if num1<num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3
#
# s = maximum(11,22,55)
# print(s)
#
# Write a python program using the function to convert Celsius to Fahrenheit
#
# def farh(cel):
#     return (cel * (9/5) + 32)
#
# f = farh(100)
# print(f)

#How do you prevent a python print() function to print a new line at the end?

# def print2(str):
#     print(str,end =' ')
#
# print2('yogesh')
# print2('is')
# print2('a')
# print2('boy')

#Write a recursive function to calculate the sum of first n natural numbers.
# def sum2(n):
#     if n == 0:
#         return 0
#     else:
#         return  n + sum2(n-1)
#
#
# a = sum2(3)
# print(a)

#Write a python function that converts inches to cms.

# def cms(inch):
#     return (inch/2.54)
#
# a = cms(1)
# print(a)

# Write a python function to print the multiplication table of a given number.
#
# def table(num):
#     for i in range(1,11):
#         print(f'{num} X {i} = {num*i}')
#
# table(5)

#Write a python function to remove a given word from a list and strip it at the same time.

def str_replace(sent,word):
    a = sent.replace('yogesh',' ')
    return a.strip()

sent = '    yogesh is a good boy   '
a = str_replace(sent,'yogesh')
print(a)