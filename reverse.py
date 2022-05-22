#to reverse the given list

lst = [1,2,3,4,5,6]

lst.reverse()

print(lst)

#to get number of string

lst = [10,20,'aaa','bbb',33.5,'ccc',88,'bbb',25]
x =0
for i in lst:
    if type(i) == str:
        x=x+1
print(x)


#3 write a program to count number of zeros in given number

x = 10203
c = 0
while(x>0):
    c=c+1
    x=x//10
print(c)

