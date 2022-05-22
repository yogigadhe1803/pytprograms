#09-01-2022


#normalization

#to elimminate code redundancy --->  inheritance and functions

#Functions --> set/group of satatements that performs a task / action.
                #like a mini program (i.e. grp of stmts)
                #code redundancy i.e. duplicasy of code will be eliminated.
                #function is a reusable piece of code.
                #a function is executed or run by the pvm only when it is called.
                #one written, function will save in memory --> port segment
                #execute in another memory called --> method stack
                #function will be stored in the memory in the form of byte code.
                #a function can return the result back --> with return stmt.
                #function can return multiple values. ex. return a,b  , return lst.
                
                #to create function-->
                def function_name(pass_the_data):
                    logic



#def ---> define a function / create a function
#parameters --> variable declared in the function to receive the data.
                
               
               
#arguments --> data/value passed to the function from outside.
              #will put value temporary in memory in the form of tuple.



#question --> what is local variable?
#answer -->local variable is a variable created in the function. 
            #the scope(availability) of local variable is limited to that function.
            #local variables are of temporary nature.
            #ones function is executed local variables are deleted/removed from the memory.


#question --> what is a global variable?
#Answer --> variable created above a function.
            #the scope(availability) of global variable is inside and also outside of the function.
            #the variable which is available inside and also outside the function.
            #global variables are stored in the global memory.
            #all global variables are stored in the form of dict(i.e. key-value pair).
            #ex .       g = 22          #GV
            #           def display():
            #               print(g)
            #           display()
            #           print(x)


#note - do not use reserved word for the program name.
        #local variables are always powerfull locally.
        #once we create a function it will internally create an object.
    


#question --> how to retrive the global variable variable in the function?
#answer --> globals()['x']



#note -->  functions are called first class objects.
            #functions and objects are equal/same.
            #can store function into a variable.
            #we can pass one function to another function.
            # x = 100    --> storing 100 as an int object in variable x
            # x = square()      --> storing square as an object in variable x.


#nested fun/inner fun --> function defined in another function.

'''
--we have to treat function as objects.

we can store a function in variable.
we can pass a function to another function.
we can write a function inside another function.
we can return a function from another function.
'''
#1
def square(x):
    return x*x

sq = square(10)


#2
def display(fun):
    res = 'Hello' + fun()
    return res
    
def myfun():
    return 'krish'


str = display(myfun)
print(str)
    #o/p --> Hellokrish



#3
def display():
    def message():
        return 'krish'
    return message() + 'na'                     #4. 
    can call another function in one function.
    
str = display()
print(str)
    #o/p --> krishna
    
    










#8. return --> useful to return the value from the function.


