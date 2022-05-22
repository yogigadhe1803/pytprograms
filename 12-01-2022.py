#12-01-2022



#lamdas ---> is a function without a name and return stmt.
            #to achive compact code.
            #every lambda is nothing but a function only.
            #every lambda internally creates an object.
            #ex. 
            #      x = lambda <parameters>: logic
            #      d = x()
            #shpuld write only in one line.
            
            #how to write if...else stmt in lambda-
            #      f = lambda <paramters>: stmt1 if cond else stmt2
            #we does not use while and for loop very often in lambda.
            #we can put everything in lambda what we can write in normal function without loop.
            #output is stored in a memory block.
            

#to use lambda on sequences -->
    #to use lambda on sequences we have to use some function.
    
#1.filter() --> filters out the elements depending on a lambda.
                #
                #syntax- 
                #        filter(lambda,sequence)
                #filter automatically applies the lambda function on sequence element by element.
                #will not do any calculation -- only filters out the elements.

#2.map()    --> filters and modifies the elements of a sequence depending on lambda.
                #syntax- 
                #       map(lambda, sequence)
                #filter + calculation
                
                
#3.reduce() --> #reduces the elements of the sequence to a single value.
                #returns only one value.
                #reduce() -- function defined in the module called functools.
                #syntax- 
                #       from functools import reduce
                #       obj = reduce(lambda,sequence)
                #       print(obj)




#note -- most interview que on -- lambda and regular expression

#__builtins__ ---> default package. we do not have to import and then call the functions in the __builtins__ package.
                #the functions that does not have to import from outside package are in this module.




#PyCharm --> is world's no. 1 IDE for python professionals according to Gartner inc., USA.
            #heavyweight(uses heavy resources)
            #only user interface. does have python software inbuilt.
            #it will check the python software in the system.(depends on python in the system)
            #so -- first install python and then install PyCharm.(so that is can detect the python software in the system)
    #breaking points- 
    
https://jumpshare.com/v/hJNbZzEERWZHhNq6jpIQ



#project in PyCharm -- nothing but a folder.
                    #if we create a project --> project = program + python software + libraries --> loaded into memory --> called virtual environment(VENV)


