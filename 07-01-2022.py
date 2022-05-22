#07-01-2022


#program saves automatically in pycharm.
#input function take the values in the form of string only.

#split() --> split method or cut the string into spaces wherever it will see the space(by default).
            #split() --> split wherever it sees space
            #split(',') --> split wherever it sees comma
            #split('\t') --> wherever it sees tab(\t)
            
            

###list comprehension --> creating to list from an iterable object.
#iterable object --> can use for loop and while.containg multiple elements.



#acepting multiple values at the same time using input function
#add three numbers

a,b,c = [int(i) for i in input("Enter three numbers = ").split()]

tot = a + b + c
print("Total = ", tot)

#o/p -->
Enter three numbers = 10 10 10
Total =  30


#
a,b,c = [int(i) for i in input("Enter three numbers = ").split('/')]
                                                               
tot = a + b + c
print("Total = ", tot)




#program
#write a python program to accept a group of elements and find their sum and average.

lst = [float(i) for i in input("Enter the numbers = ").split()]

s = sum(lst)
a = s/len(lst)

print("sum = ", s)
print("Average = %.4f" % a)

#o/p -
Enter the numbers = 20 3 30 20  10
sum =  83.0
Average = 16.6000





#accept a group of numbers from keyboard and sort them into ascending order.
#1st approach
lst = [int(x) for x in input("Enter the elements = ").split()]
lst.sort()
print(lst)

#o/p -
Enter the elements = 20 20 20 20 30 1 2 5 3 40
[1, 2, 3, 5, 20, 20, 20, 20, 30, 40]



#2nd approach
lst = [int(x) for x in input("Enter the elements = ").split()]
lst.sort()
for i in lst: print(i, end=' ')

#o/p -
Enter the elements = 1 2 9 8 7 5 2 1 11 35 422
1 1 2 2 5 7 8 9 11 35 422 




#sequential/linear execution --> executing the statements linearly(one by one).
                                #useful to develop simple programs only.
                               

#random execution --> executing the statements randomly and repeatedly.
                    #useful to develop critical or complex programs.
                    #random exec is possible by using control statements.



#convention --> for constant write variable in all caps.


#control statements --> are the statements that control the flow/logic of execution.
                        #connot develop complex program without control statements.


#1. if..elif..else stmt :
 
if cond:
    stmts
    
    
    
if cond:
    stmts
else:
    stmts



if cond:
    







'''
program statement
author: name
version: v1.0
company: company name
project title: 
code: 
'''

