num = [1,2,2,3,2,3,4,5,6,7,8]
alph= [1.1,2.2,3.3,4.4]

print(num[-2])  # from reverse side

print(num[2:5]) #0[ 3,4,5] i.e index 1 include and index 5 exclude

print(num[:2]) # from start upto 2
print(num[3:]) # from 3 to onward

print(num[::2])  #means it leaves every second one

# List functions 

num.extend(alph)    #it append another list at the end

num.append(9)   #it append value at the end

num.insert(3,0)     #it insert value at specific position i.e the 1st num is postion the second will value

num.remove(3)   #remove specific value

num.pop()   #remove last value and return it

# num.clear()     #clear all list

print(num)

print(num.index(2)) # give the index of the specific value
print(num.count(2))     #give the count that how much one value is repeated 

num.sort()  # ascending order same for alphabetical

# b = l4[::-1] # in reverse but not the proper way

num.reverse()

num2 = num.copy()   #if only write num2 = num it will not work i.e whenever i append something to num2 it will be also appended to num b/c 
# num2 = list(num) # method for copying
# num2 = num[:] # method for copying

v = [45,5]
v2 = v
v2[1] = 4 #here v2 refer to the list object i.e output of both will be same
print(v)
print(v2)



# 2d list and nested loops
print("printing 2dlist")
two_d_list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,11,12]
]

print(two_d_list[0][0])

for row in two_d_list:
    print(row)

for row in two_d_list:
    for col in row:
        print(col)    



# List comprehension
# making a new list from existing list in one line
l6 = [1,2,3,4,5]
l7 = [i*1 for i in l6]      # 1,4,9,36.........


