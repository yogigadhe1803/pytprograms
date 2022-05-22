#04-01-2022


#in python, double quote and single quote are treatded same.


#Datatypes in Python

#datatype -- type of data stored into a variable/memory.



#variable can be --> x, x1, x_1, _x1
                    #but cannoot start with number.
                    
                    
                    
                    
#ex. x = 10
#memory address stored in x.
#10 stored in memory.
#10 is interger and stored in x ----> this means ---> x is int datatype/type variable.



#integer --> number without decimal. ex. 100, -125, 162738 etc
#floating point --> number with decimal. ex. 100.5, -9.8, 100.0 etc
#string --> group of charecters string. ex. 'name', 'yogesh' etc
#boolean --> can store either true or false. ex. x = True --> x is bool type variable.




#>>type()
#question --> how to check the datatype of a variable?
#answer --> type() ---> will show/display the datatype of a variable.
            # x = 10 ----> type(x) ----> <class 'NoneType'>
>>> type(10.5)
<class 'float'>
>>> type(10)
<class 'int'>
>>> type('yogesh')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type(None)
<class 'NoneType'>
>>> 








#question--> can i call a class a datatype?
#answer--> yes, a class is called user defined datatype.




#programmer did not have to declare the datatype of a variable.





##Datatypes in python

#1.NoneType --> nothing is stored in datatype
                # we store None in variable.
                #ex. x = None
                
>>>x = None
>>>x 
>>>print(x)
None
>>>type(x)
<class 'NoneType'>



#2.Numaric datatypes --> 

    #A. integer ---> number without decimal point.               
                #
>>> x = 125
>>> x
125
>>> print(x)
125
>>> type(x)
<class 'int'>
                 


    #B. float ---> number with decimal point.
                #ex. x = 10.5 
>>> x = 12.5
>>> x
12.5
>>> print(x)
12.5
>>> type(x)
<class 'float'>
>>>

    #C. complex -->
            #number which is written in the form of a +- bj.
            # where a --> real part, b --> imaginary part, j --> sq. root of -1
            #can use capital J or small j.
>>> x = 5 + 4j
>>> y = 6 - 7J
>>> x
(5+4j)
>>> y
(6-7j)
>>> type(x)
<class 'complex'>
>>> type(y)
<class 'complex'>
>>> x + y
(11-3j)
>>> x - y
(-1+11j)
>>> x * y
(58-11j)
>>> x / y
(0.02352941176470587+0.6941176470588236j)
>>> 





#3.Boolean datattype --> bool
                    #two values  ---> True , False
>>> a = True
>>> b = False
>>> a
True
>>> b
False
>>> a and b
False
>>> a and a
True
>>> b and b
False
>>> a or b
True
>>> a or a
True
>>> b or b
False
>>> not a
False
>>> not b
True
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>                    





#4.Sequences ----> represents a group of elements.
                   #ex. group of numbers/charecters/bool.
                   
            #A. str datatype ---> group of charecters.
                            #have to give either "" or ''
                            #ex. 'Nagesh' , "abc123" , '1bc_?>@#'
                            #space is also taken as charecter in string.
                            #str stored in single quote('')
                            #multi-line str --> should use in tripple single quote('''value''') or double quote("""value""")

#position of substr in str
#will give the number of first occurance
str.index('is', 3)  #at the place of 3 --> by default 1
5

#count the number of times substr is repeated.


>>> s1 = "Hello"
>>> s1
'Hello'
>>> print(s1)
Hello
>>> s2 = 'hai'
>>> s2
'hai'
>>> print(hai)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hai' is not defined
>>> print(s2)
hai
>>> book = 'This is a "Core Python" text book'
>>> book
'This is a "Core Python" text book'
>>> print(book)
This is a "Core Python" text book
>>> s3 = '''aakhfbahkfbkabfkbak '''
>>> s3
'aakhfbahkfbkabfkbak '
>>> len(book)
33
>>> s4 = 'Hydera'+"bad"
>>> s4
'Hyderabad'
>>> print(s4)
Hyderabad
>>> str = 'Vijay Kumar'
>>> str.upper()
'VIJAY KUMAR'
>>> str.lower()
'vijay kumar'
>>> book.title()
'This Is A "Core Python" Text Book'
>>> name = "   Vijay kumar "
>>> name
'   Vijay kumar '
>>> name.lstrip
<built-in method lstrip of str object at 0x000002DA6468F4B0>
>>> name.lstrip()
'Vijay kumar '
>>> name.rstrip()
'   Vijay kumar'
>>> name.strip
<built-in method strip of str object at 0x000002DA6468F4B0>
>>> name.strip()
'Vijay kumar'
>>> str = 'This is a book'
>>> str.index('is')
2
>>> str.index('is', 3)
5
>>> str.find('is', 3)
5
>>> str.find('is')
2
>>> str.count('is')
2
>>> str
'This is a book'
>>> str.replace(' is ', ' was ')
'This was a book'
>>>










##note-
#function and method both are same. with one difference.

#function --> grp of statements(mini program)
            #to call --> fun()

#method --> function written inside a class.

#to call fun --> fun()
    #ex.  len(str)
       
#to call method --> class.fun()  or object.fun()
    #ex. str.upper()
    
#object --> memory
#class --> structure/blueprint to creating a object.
            #class means group. 










####very Important####

#Basic Operarions on sequence.
#1. indexing --> retriving a element by its position number. 
                []
                #ex. str[0]
>>> str
'This is a book'
>>> str[0]
'T'
>>> str[1]
'h'
>>> str[2]
'i'
>>>


#2.slicing --> retriving a range of elements.                                 --->  (5 out of 15 questions are on slicing)
                #retriving 5th to 10th elements.
                # str[starting index number : ending index number : step size]
                #ex. str[0:4:2]  --> 1 at the place of 2 by default.
                #last index is excluded. i.e. str[0:4:2]  --> index 4 will be excluded.
                #default number of ending index --> position of last charecter.
                #if ending index not given --> automatically goes to the last charecter.
                #if starting index is not given --> automatically takes from 0th index.
                
    #forward slicing  --> retriving from left to right. default starting index --> first char 
                                                       #default ending index --> last char
                                                       
    #back slicing  --> retriving from right to left. ---> must have to take step size and in negative.
                                                        #default starting index --> last charecter
                                                        #default ending index --> first charecter 
               
>>> str
'This is a book'
>>> str[0:3]
'Thi'
>>> str[0:4]
'This'
>>> str[]
  File "<stdin>", line 1
    str[]
        ^
SyntaxError: invalid syntax
>>>
>>>
>>>
>>>
>>>
>>>
>>> str
'This is a book'
>>> str[0:3]
'Thi'
>>> str[0:4]
'This'
>>> str[5:7]
'is'
>>> str[10:len(str)]
'book'
>>> str[10:]
'book'
>>> str[0:4]
'This'
>>> str[:4]
'This'
>>> str[:]
'This is a book'
>>> str[0:14:2]
'Ti sabo'
>>> str[13:9:-1]
'koob'
>>> str[3::-1]
'sihT'
>>> str[::-1]
'koob a si sihT'
>>>







#3.repeatation ---> to repeate the sequence n times.
                    # * is used.
                    # ex.  str * 2      ---> string will repeate 2 times.
>>> str * 2
'This is a bookThis is a book'
>>> 2 * str
'This is a bookThis is a book'
>>>

























#question --> how python automatically takes the datatype?
#answer -->








