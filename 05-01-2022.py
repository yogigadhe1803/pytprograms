#05-01-2022


#online.datatechs.in


#Datatypes in python




#char datatype --> represents a single character

#note
#there is no char datatype in python.
#we should use str datatype to represent single character.
#in ---> operator
#indentation --> leaving 4 spaces.




#question --> is there any datatype to represent single charecter in python?
#answer --> no. but we can use str datatype.




#loop --> will execute repeatedly
#2.while loop
#1.for loop
        #syntax -       for var in seq:          ---> header part
        #                    statements         ---> body part(statement should start with 4 spaces --> otherwise it will not consider statement in loop )
        
        #number of times loop executes = number of elements in the sequence 
        #ex.
>>> str = 'hello'
>>> print(str)
hello
>>> for i in str:
	print(i)

	
h
e
l
l
o
>>> for i in str:
	print(i)
	print("yes")

	
h
yes
e
yes
l
yes
l
yes
o
yes



#to avoid the porblem of charecter going in next line
>>> for i in str:
	print(i, end='')         #By default end='\n'

	
hello
>>> for i in str:
	print(i, end='')

	
hello
>>> for i in str:
	print(i, end=' ')

	
h e l l o 
>>> 


#end is an attribute. (by deafault --> \n is taken in end bute. i.e. end ='\n')
#attribute --> extra information provided to the function.








    #B. Byte datatype --> group of byte numbers.
                    #Byte number --> number in the range of 0 to 255.(2^8)
                    #cant modify the elements(immutable).
                    #cant use slicing or repetation on byte datatype.
                    
>>> b = bytes([20, 35, 44, 0, 200, 255, 16])
>>> b
b'\x14#,\x00\xc8\xff\x10'         #memory 
>>> for i in b:
	print(i)

	
20
35
44
0
200
255
16
>>> b[0]
20
>>> b[1]
35
>>> b[0:3]
b'\x14#,'
>>> b*2
b'\x14#,\x00\xc8\xff\x10\x14#,\x00\xc8\xff\x10'
>>> b.add(10)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b.add(10)
AttributeError: 'bytes' object has no attribute 'add'
>>> b[0]
20
>>> b[0] = 200
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b[0] = 200
TypeError: 'bytes' object does not support item assignment
>>> 






    #C .Byte Array --> can be modified
>>> ba = bytearray([33, 44, 55, 66, 77])
>>> ba[0]
33
>>> ba[0] = 100
>>> for i in ba: print(i)

100
44
55
66
77
>>> ba.add(100)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ba.add(100)
AttributeError: 'bytearray' object has no attribute 'add'
>>> ba.append(100)                                          #to add new elements in bytearray
>>> print(ba)
bytearray(b'd,7BMd')
>>> for i in ba: print(i)

100
44
55
66
77
100
>>> ba
bytearray(b'd,7BMd')
>>> 






#que --> difference between byte and bytearray?
#answer --> byte datatype --> cannot be modified --> i.e. immutable
            #bytearray datatype --> can be modified --> i.e. muta
            







      #D .list datatype --> a group of elements of various datatype.
                #versetile datatype.\
                #list are identified by a square bracket --> []\
                #list are mutable.
                
>>> lst = []   #to create empty list.
>>> lst
[]
>>> lst =[10]
>>> print(lst)
[10]
>>> mylst = [10, 20, 33, 45.5, -22, 'srinu', "x"]
>>> mylst[0]
10
>>> mylst[0] = 100                              #to modify/ change already existing element.
>>> mylst
[100, 20, 33, 45.5, -22, 'srinu', 'x']
>>> del(mylst[5])                               #to delete element using index number.
>>> mylst
[100, 20, 33, 45.5, -22, 'x']
>>> mylst.remove('x')
>>> 
>>> mylst
[100, 20, 33, 45.5, -22]
>>> mylst.append(88)
>>> mylst
[100, 20, 33, 45.5, -22, 88]
>>> mylst.insert(1,22)
>>> mylst
[100, 22, 20, 33, 45.5, -22, 88]
>>> mylst.insert(4,333)
>>> mylst
[100, 22, 20, 33, 333, 45.5, -22, 88]
>>> x = [1, 2, 3]
>>> mylst.extend(x)
>>> mylst
[100, 22, 20, 33, 333, 45.5, -22, 88, 1, 2, 3]
>>> mylst.index(22)
1
>>> mylst.index(333)
4
>>> mylst.count(45.5)
1
>>> mylst.reverse()
>>> mylst
[3, 2, 1, 88, -22, 45.5, 333, 33, 20, 22, 100]
>>> mylst.sort()
>>> mylst
[-22, 1, 2, 3, 20, 22, 33, 45.5, 88, 100, 333]
>>> mylst.sort(reverse=True)
>>> mylst
[333, 100, 88, 45.5, 33, 22, 20, 3, 2, 1, -22]
>>> mylst[0]
333
>>> mylst
[333, 100, 88, 45.5, 33, 22, 20, 3, 2, 1, -22]
>>> mylst[0:4]
[333, 100, 88, 45.5]
>>> mylst[8:11]
[2, 1, -22]
>>> mylst[8:]
[2, 1, -22]
>>> mylst[::2]
[333, 88, 33, 20, 2, -22]
>>> mylst[10:7:-1]
[-22, 1, 2]
>>> mylst[2::-1]
[88, 100, 333]
>>> mylst[::-1]
[-22, 1, 2, 3, 20, 22, 33, 45.5, 88, 100, 333]
>>> mylst = [100, 20, 30, 4, 5.2, -22]
>>> max(mylst)
100
>>> min(mylst)
-22
>>> sum(mylst)
137.2
>>> len(mylst)
6
>>> mean(mylst)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    mean(mylst)
NameError: name 'mean' is not defined
>>>






#question --> difference between del() and remove()
#answer -->del() is a function. remove is a method
            #in del()  --> have to give position number.
            #in remove() --> have to give name of element.



#append --> add at the end.
#insert --> add in between.
#extend --> to add two list.
#index or find --> to know the position number of the element.
#count --> to count the number of occurance.
#reverse --> reversing the list.  (reversing is not sorting)
#sort --> only work on numerical.
#delete --> delete the element.










#question --> how to create doubly linked list?
#answer --> simply create using list.  ex. lst = [2, -1, 52.2, 'hey', "aj"]








        #E .tuple datatype --> same as list but cannot be modified
                    #tuples are immutable.
                    #for security.
>>> tpl = ()    #to create empty tuple.
>>> tpl
()
>>> tpl = (10, )        #to create tuple with single element(comma is compulsary)
>>> tpl
(10,)
>>> tpl = (10, 20, 3.56, 'srinu', 'x')
>>> tpl
(10, 20, 3.56, 'srinu', 'x')
>>> for i in tpl: print(i)

10
20
3.56
srinu
x
>>> 



#question --> what is the difference between list and tuple
#answer --> both list and tuples are same to store the different datatypes.
            #one difference --> list --> mutable
                                #tuple --> immutable
                                #list --> [] 
                                #tuple --> ()



#object --> memory block





        #F .range datatype --> is infact a function.
                    #generates a sequence of numbers.
                    #ex.   range(10)  --> will generate 0 to 9
                          #range(10,20)  --> will generate 10 to 19
                          #range(10,20,2) --> 10, 12, 14, 16, 18

>>> r = range(10)
>>> r
range(0, 10)
>>> for i in r: print(i)
...
0
1
2
3
4
5
6
7
8
9
>>> for i in r: print(i, end='')
...
0123456789>>>
>>> for i in range(10): print(i)
...
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10,21):
...     print(i)
...
10
11
12
13
14
15
16
17
18
19
20
>>> for i in range(10,21,2):
...     print(i)
...
10
12
14
16
18
20
>>> for i in range(10,0,-1): print(i)
...
10
9
8
7
6
5
4
3
2
1
>>>








####5.SETS
        #A. set datatype --> represents unordered collection of data.
                    #sets do not store duplicate elements.
                    #{} or can use set() function
                    #can store various type of elements.
                    #the same order is not maintained ehile storing in a memory.
                    #indexing, sli, repetation operations cannot be does on sets.
                    #can modify set(mutable).
                    #cannot use del() function but revome() can work.
                    #can use sets when we need unique elements.
>>> s = {10, 20, 30, 40, 'srinu'}
>>> print(s)
{20, 40, 10, 'srinu', 30}
>>> s.add(100)
>>> del(s[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object doesn't support item deletion
>>> s.remove('srinu')
>>> s
{20, 100, 40, 10, 30}
>>> s.add(100)
>>> s
{20, 100, 40, 10, 30}
>>>




        #B .frozenset --> same as set but cannot be modified(immutable).
                    #convert frozenset to set to modify it.
                
>>> s
{20, 100, 40, 10, 30}
>>> fs = frozenset(s)
>>> fs
frozenset({20, 100, 40, 10, 30})
>>> fs.add(22)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>>





#question--> difference between set and frozenset
#answer --> same ---> will not maintain orderlyness in elements
#           one difference --> sets --> mutable
                                #frozenset --> immutable


#for loop --> can use on any object that contian grp of elements.







#mapping datatype --> maps (or links) a key with its value.

####6.dict datatype --> stores in the form of key-value pairs.
                    #key and value are saperated by :
                    #can modify through key only.
                    #key-value pair is counted as one element.
>>> st = {10:'Raju', 11:'Laxmi', 12:'Vinay', 13:'Anil'}
>>> type(st)
<class 'dict'>
>>> st
{10: 'Raju', 11: 'Laxmi', 12: 'Vinay', 13: 'Anil'}
>>> name = st[11]
>>> name
'Laxmi'
>>> st[11] = 'sita'
>>> st
{10: 'Raju', 11: 'sita', 12: 'Vinay', 13: 'Anil'}
>>> st[20] = 'Rao'
>>> st
{10: 'Raju', 11: 'sita', 12: 'Vinay', 13: 'Anil', 20: 'Rao'}
>>> del(st[11])
>>> st
{10: 'Raju', 12: 'Vinay', 13: 'Anil', 20: 'Rao'}
>>> len(st)
4
>>> st
{10: 'Raju', 12: 'Vinay', 13: 'Anil', 20: 'Rao'}
>>> k = st.keys()
>>> k
dict_keys([10, 12, 13, 20])
>>> for i in k: print(i)
...
10
12
13
20
>>> v = st.values()
>>> v
dict_values(['Raju', 'Vinay', 'Anil', 'Rao'])
>>> for i in v: print(i)
...
Raju
Vinay
Anil
Rao
>>> for i in st.values(): print(i)
...
Raju
Vinay
Anil
Rao
>>> for k, v in st.items(): print(k, v)
...
10 Raju
12 Vinay
13 Anil
20 Rao
>>>
