#13-01-2022


#array -- > represents a group of elements of same datatype.
            #array stores the elements in side by side memory locations.
            #arrays are faster compare to the list.
            #default datatype used for numerical arrays in numpy --> float
            #datatype of numpy array --> ndarray    (n dimensional array)



#question --> default datatype used for numerical arrays in numpy?
#answer --> float

#question --> datatype of numpy array?
#answer --> ndarray

#numpy --> package developed by third party vendors to deal with arrays(especially multidimensional(2D-3D) arrays)

#types of arrays - 
#1. single dimensional arrays --> represents only one row or column of elements.
                            #ex. marks obtained by a student in 5 subjects.
                            #       [50, 20, 30, 50, 38]
                            #               or
                            #       [50,
                            #        20,
                            #        30,
                            #        50,
                            #        38]
    #creating 1D arrays -
        #1. array()   -- function
                    #ex. a = numpy.array([20, 30, 60, 50, 60])
                    
        #2. linspace()  -- linear space. 
                    #ex. ln = linspace(0,10,5)  --> from 0 to 10 and divided into 5 parts
                    #internally stores as float.
                    #divides equaly
                    
        #3. logspace()  -- used by data scientist.
                    #creats according to the log i.e. poer of 10 
                    #ex. b = numpy.logspace(0,10,5)

        #4. arange() -- similler to range function.
        
        #5. zeros -- to create array with all zero as elements.
                    # b = zeros(5, int)     --> to make elements int
        
        #6. ones -- to create array with all one as elements.
    
    
    #operations on array-
        #type(arr)
        
        #arr+5, arr-5, arr*6, arr/3

        #sqrt(arr)
        
        #pow(arr, 3)    --> elements to the power of 3

        #sum(arr) 
        
        #max(arr)
        
        #min(arr)
        
        #np.argmax(arr)
        
        #np.argmin(arr)
        
        #np.sort(arr) -- ascending
        
        #np.sort(arr)[::-1]  -- descending
        
        #indexing --> arr[0], arr[1]
                                            #do not support repeatation.
        #slicing --> arr[0:5:2]                 
        
 >>> from numpy import *
>>> arr = arange(10,21,2)
>>> type(arr)
<class 'numpy.ndarray'>
>>> arr+5
array([15, 17, 19, 21, 23, 25])
>>> arr-5
array([ 5,  7,  9, 11, 13, 15])
>>> arr*5
array([ 50,  60,  70,  80,  90, 100])
>>> arr/5
array([2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> sqrt(arr)
array([3.16227766, 3.46410162, 3.74165739, 4.        , 4.24264069,
       4.47213595])
>>> pow(arr,3)
array([1000, 1728, 2744, 4096, 5832, 8000], dtype=int32)
>>> sum(arr)
90
>>> max(arr)
20
>>> min(arr)
10
>>> argmax(arr)
5
>>> argmin(arr)
0
>>> sort(arr)
array([10, 12, 14, 16, 18, 20])
>>> sort(arr)[::-1]
array([20, 18, 16, 14, 12, 10])
>>> arr[2]
14
>>> arr[0:5:2]
array([10, 14, 18])
>>>     
        
    #copying array -->
        #a = arr  --> will give name to same memory block.  
                    #will not copy the data into a.
                    #if we modify new array (i.e. a) the original also modifies and vice versa.
                    
        #arr.view() --> data will be copied into new arrray. 
                    #saperate memory block will be allocated to new array.
                    #but their will be some internal linking into those 2 arrays.
                    #this is known as shallow copying.
                    #shallow copying -- after copying the array if we modify original array, the new array will also be modified and vice versa.
        
        #arr.copy() --> will completly copy the arr to new array.
                    #deep copy --> if we modify new array, the original array will not be affected and vice versa.
                    

#question -> diff between shalow copy and deep copy?
#answer ->



    #attributes(properties) of an array --> property looks like a variable but works like a method.
        #arr.ndim --> returns the type of an array.
>>> arr
array([10, 12, 14, 16, 18, 20])
>>> arr.ndim
1
>>> b
array([[1, 2, 3],
       [5, 6, 7]])
>>> b.ndim
2
>>> 


        #arr.shape --> gives the nunmber of rows and columns of an array.
>>> b
array([[1, 2, 3],
       [5, 6, 7]])
>>> b.shape
(2, 3)
>>>         

        #arr.size -->no. of elements
        
        
        #arr.itemsize --> size of each element
        
        
        #arr.dtype --> datatype of an array
        
        #arr.nbytes --> total size of an array.
        
        
        
        
        
        #arr.reshape() --> converts 1D array into 2D array. no. of elements should be same after reshaping.
>>> arr
array([10, 12, 14, 16, 18, 20])
>>> arr.reshape(2,3)
array([[10, 12, 14],
       [16, 18, 20]])
>>> arr.reshape(3,2)
array([[10, 12],
       [14, 16],
       [18, 20]])
>>> 


        #flatten() --> converts 2D array into 1D array
>>> b
array([[1, 2, 3],
       [5, 6, 7]])
>>> b.flatten()
array([1, 2, 3, 5, 6, 7])
>>>         


   
   
   
   
   
#2. multidimensional arrays.(2D) --> represents more than one row or column of elemets.
                        #ex. marks of 3 students in 5 subject.
    #create 2D array -
    
            #1. array() --
>>> arr = array([[1,2,3],[4,5,6],[7,8,9]])
>>> arr
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> 

            #2. ones() -- ex. arr = ones((rows,col),datatype)
            
            #3. zeros() --
            
            
            #4.eye() -- arr = eye(5, dtype= int)  --> will create an array of 5 rows and 5 column of int datatype.
                        #create square type array --> diagonal elements filled with 1 and remaining elements filled with 0.
    
    
    
    #operations on 2D array -
            #1. indexing - 
                        # arr[0] --> total 0th row
                        # arr[0,0] --> element in 0th row and 0th column
                        
            
            #2. slicing -- arr[r1:r2 , c1:c2]
                        #arr[0:2,0:2]  --> 0th row to 1st row and oth col to 1st col.
>>> arr
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> arr[0:2,0:2]
array([[1, 2],
       [4, 5]])
>>> arr[:2,:2]
array([[1, 2],
       [4, 5]])
>>> arr[:,2:]
array([[3],
       [6],
       [9]])
>>>  

                      
            
            #3. sum()
            
            #4. mean()
            






#matrix  --> represents collection of elements arranged in several rows and cols.
            #matrix with only one row --> row matrix    (1D array)
            #matrix with only one col --> column matrix (1D array)
            #matrix with m rows and n col --> mXn matrix   (2D array)
            
    #creating a matrix -> matrix()
    #   matrix(string)
>>> str = '7 8 9; 2 0 2; 5 -5 1'
>>> m = matrix(str)
>>> m
matrix([[ 7,  8,  9],
        [ 2,  0,  2],
        [ 5, -5,  1]])
>>> 


    #   matrix(2D array) 
>>> arr
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> mt = matrix(arr)
>>> mt
matrix([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
>>> 
    
    
    #operations -
            #m1*m2 -> multiply two matrices
            #m1+m2
            #m1/m2
>>> m1
matrix([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
>>> m2
matrix([[ 7,  8,  9],
        [ 2,  0,  2],
        [ 5, -5,  1]])
>>> 

            #m1.tranpose() or m1.T -
                            #
>>> m1
matrix([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
>>> m1.T
matrix([[1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]])
>>> 




    #how to input data into matrix from keyboard.