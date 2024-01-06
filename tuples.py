import sys
import timeit
# a container that store different values, immutable,ordered and can have duplicate elements
t1 = (1,2,3,5,5,5,5,) 
l1 = [1,2,3]
print(t1.count(5)) # 4
print(t1.index(5)) # 3 eturn the first occurance
t2 = tuple(l1) # makes it tuple
coordinates = [(1,2),(1,3),(1,4)] 

print(coordinates[1])
print(coordinates[0])
# //////////////////////////////////////////////////////////////////////////////////////
# slicing same as in list 

# unpacking tuple 

tp1 = ("rahim" , "23")
       
name, age = tp1
print(name) #rahim
print(age)  #23
# ////////////////////////////////////////////////////////////////////////////////////


tple = (1,2,3,4)

i1,*i2,i3 = tple

print(i1)       # 1 the very first item 
print(i2)      # 2,3 will make the lsit of midle items of first and last
print(i3)       # 4 the very last item

# ////////////////////////////////////////////////////////////////////////////////////


list1 = ["hello",1,2,3,True]
tple1 = tuple(["hello",1,2,3,True])



print(sys.getsizeof(list1),"bytes")
print(sys.getsizeof(tple1),"bytes")     #tuples posses less space than list and is more efficent than list while dealing large data

print(timeit.timeit(stmt="[1,2,3,4,5,6]",number=10000000))
      
print(timeit.timeit(stmt="(1,2,3,4,5,6)",number=10000000)) #if we repeat the give number 10000000 time the list creation will take 0.3 greater time than tuple

# ///////////////////////////////////////////////////////////////////////////////////