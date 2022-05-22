#11-01-2022




#recusrsive function --> a function that calls itself.(phenomenon called recursion)


#programs that uses recusrsive function --
#1.factorial of a number(ex. 4!, 56!, etc.)(note - !0 = 1)

    #logic -
if n == 0:
    then res = 1
else:
    res = n * fact(n-1)



#towers of hanoi





#parameter/formal argument --> argument that is declared into the function.
                    #parameters and arguments are same.
                    #receives the data when the function is called.

#argument/actual argument --> actual data passed to the function.



#four types of arguments -->

#1.positional arguments --> arguments passed in the correct order/position.
                        #if you change the order/position, the ouput also changes.
    #ex.
def join(a,b):
    c = a + b
    print(c)

join('Auranga','bad')       #positional arguments

join('bad','Auranga')       #order changed so the output




#2.Keyword arguments --> which are passd by identifying parameter names.
                        #have to use parameter name also.
                        #eventhough we change the order, still the result will be same.
    #ex.
def join(a,b):
    c = a + b
    print(c)

join(a= 'Auranga',b='bad')       #keyword arguments

join(b='bad',a='Auranga')       #order changed but will not affect the output.




#3.default arguments --> the argument which take/uses default value if not given.
                        #default value -- value that is used by default by the parametr
    #ex.
def grocery(item, price= 50.00):
    print('Item name = ', item)
    print('Price= %.2f' % price)


grocery('sugar')
#o/p -  Item name= sugar 
#       Price= 50.00
 
grocery('oil',55.60)
#o/p -  Item name= oil 
#       Price= 55.60
 
 
 
#4. variable length arg --> arg that can store 0 or more values(multiple values).
                        #have to use * symbol before argument. ex.  *x  , *a , etc.
                        #will stil work eventhough we did not gave the value.
    #ex.
def add(n, *x)          #x is internally a tuple.
    total = n + sum(x)
    print('Total = ',total)

add(100, 10, 11, 12)        #100 stored into n and 10, 11, 12 stored into x
add(100)                    #will take 0 by default






#function decoretor --> decoretor is a function that decorates another function.
                    #i.e. modifies the result of another function. 
                    #sometimes modifies the nature of the another function.
                    #can modify the function without modifying the code of the function.
                    #decoretor takes a function as its parameter and returns another function.

def decor(func1):
    
        
    return func2



#generator function --> func that generates a sequence/range of numbers.
                    #generator function will return object/memory block which contain the result.
                    #range() is a generator function.



#question --> what is decoretor? --> modifies a function
#question --> what is generator? --> generates sequence/range of numbers.


#yield --> sends the o/p to a memory block/object.
#google it >> #stack --> LIFO model



# . --> membership operator



#module ---> a module is a python program that contains variables, functions, classes etc.(contains anything we can write in a program)
            #can be imported into other progrmas.
            #property --> reusibility.
    #four types to import a module which is in the same folder as the program.
    #1. import math
    #   a = math.sqrt()
    
    #2. import math as m        #using alias name
    #   a = m.sqrt()
    
    #3. from math import *      #do not have to write module name or alias before function.
    #   a = sqrt()

    #4. from math import add, sqrt, sub     #call only specific functions
    #   a = sqrt()





#package --> is a folder that contains one or more modules.

#note -
#have to create python program (which is empty) so that the PVM can understand the folder is a package.
# __init__.py       -- 0Byte
    
    #four diff waysto import from a package.
    #1. import package.module
    #   a = package.module.function()

    #2. import package.module as ar
    #   a = ar.function()
    
    #3. from package.module import *
    #   a = function()
    
    #4. from package.module import fun1(), func2()
    #   a = fun1()



#library --> a collection of packages.


#API (application program interface)--> contains descreption of all the features of the software






#question --> can you understand the python code written by other programmers? 
#answer --> yes. coz i have worked with several libraries like numpy, pandas, matplotlib.
            #and analysed the lot of programs also.
            
#question --> google people developed a library as follows. tell us how can you use that library in you program?
             #  google/en/gui/py310/10/colors.py
#answer -->  #colors.py --> module  fun1 --> function in that module
            
            #to import (1st way) -->
              import google.en.gui.py310.10.colors
            #to use -->
                google.en.gui.py310.10.colors.fun1()
            
            
            #2nd way --> 
                google.en.gui.py310.10.colors as cl
                
               cl.fun1()
               
            #3rd way
            
            #4th way