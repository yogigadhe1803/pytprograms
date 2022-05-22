#06-01-2022



#variable --> name of memory location to store the data
#Literal --> constant value stored into a variable.

a = 10
#a --> variable
#10 --> integer literal
a = 15.55  #--> float literal
a = 'srinu'  #--> string literal


#magic method


operator #--> symbol that performs an operation.
operand #--> data on which the operator acts.



1. arithemetic operators 
a + b
#internally a hidden function is called
# + --> addition operator
#a and b --> operand




a = 13; b =5
# ; --> to write multiple statements in one line

# // --> integer division or floor division
# ** --> power operator or exponant operator
# %  --> modulus operator

>>> a = 13 ; b = 5
>>> a + b
18
>>> a - b
8
>>> a * b
65
>>> a / b
2.6
>>> a // b
2
>>> a ** b
371293
>>> b ** 3
125
>>> a % b
3
>>> 






# = --> storage operator or assignment operator. 

# += 
# -= 
# /= 
# *= 




>>> x = 10
>>> x += 10
>>> x
20
>>> x -= 10
>>> x
10
>>> x /= 10
>>> x
1.0
>>> x *= 10
>>> x
10.0
>>>



#program
#0 --> zero
#10 --> ten
#125 --> One Hundred and twenty five


#program
#enter first number : <multi line number>
#enter second number : <multi line number>
#should display the correct addition till last digit




>>> a,b,c,d = 1,2,3,4.5
>>> print(a,b,c,d)
1 2 3 4.5               #by default sep = space. we can custom it by sep=''
>>> a=b=c=d=100
>>> print(a,b,c,d)
100 100 100 100
>>>




comparison operator --
# == --> equal to
# != --> not equal to



logical operator
# and 
# or
# not



#input --> data given to a program 

#input() --> to take the input
#print() --> to display the output/results.

#sep --> to saperate multiple values in same print function.





#print() -->
#when comma then by default space in output.

>>> print('R nageshwar rao')
R nageshwar rao
>>> print('abfkjab>?><>">"6463')
abfkjab>?><>">"6463
>>> sal = 15222.161
>>> print(sal)
15222.161
>>> print('Your salary is Rs. ',sal)
Your salary is Rs.  15222.161
>>> a,b,c,d = 1,2,3.5,'srinu'
>>> print(a,b,c,d)
1 2 3.5 srinu
>>> print(a,b,c,d, sep=',')
1,2,3.5,srinu
>>> print(a,b,c,d, sep=',  ')
1,  2,  3.5,  srinu
>>> print(a,b,c,d, sep='*****')
1*****2*****3.5*****srinu
>>> print(a,b,c,d, sep='\n')
1
2
3.5
srinu
>>> print(a,b,c,d, sep='\t')
1       2       3.5     srinu
>>>




#format string
# %i  --> integer
        # %10i  --> will take 10 spaces.
        
# %s --> string (should display the string at left side)
        # %15s  --> will take 15 spaces
        # %-15s  --> will take 15 spaces but print the string at left side.
        
# %f --> float  (will display 6 digits after decimal point)
        # %.2f --> will display 2 digits after decimal point
        # %10.2f  --> total 10 spaces (including digits after decimal point)
        
        
        



# {}  --> python place holder

id = 10
name = 'srinu'
sal = 35462.23

print('Id=',id,'Name=',name,'salary=',sal)

print('Id=%i,name=%s,salary=%.2f' % (id,name,sal))

print('Id=%5i,name=%-15s,salary=%10.2f' % (id,name,sal))

print('Id={},name={},salary={}'.format(id,name,sal))

print('Id={2},name={0},salary={1}'.format(id,name,sal))

print('Id={:5d},name={:15s},salary={:10.2f}'.format(id,name,sal)) 




###
a,b,c =10, 20, 30 
print('%d %d %d\n'%(a,b,c))

print('%d\n%d\n%d\n'%(a,b,c))

print('%d\t%d\t%d\n'%(a,b,c))

print('%d\\%d\\%d'%(a,b,c))

print('%d %d %d'%(a,b,c))







##input function --> input data from keyboard.
# 

str = input("Enter a string: ")
print('You Entered : ', str)

#to accept a single character 
str = input("Enter a string: ")
print('You Entered : ', str[0])


#to accept an integer number


n = int(input("Enter an int = "))
print('U entered =', n)
print('U entered = %d' % n)
print('U entered = {}'.format(n))



#to accept an float number


n = float(input("Enter an int = "))
print('U entered =', n)
print('U entered = %f' % n)
print('U entered = {}'.format(n))