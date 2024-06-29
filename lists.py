num = [1,2,2,3,2,3,4,5,6,7,8]
alph= [1.1,2.2,3.3,4.4]
print(num[-2])  # from reverse side

print(num[2:5]) #0[ 2,3,2] i.e index 1 include and index 5 exclude



print(num[:2]) # from start upto 2
print(num[3:]) # from 3 to onward

print(num[::2])  #means it leaves every second one

# List functions 

num.extend(alph)    #it append another list at the end

num.append(9)   #it append value at the end

num.insert(3,0)     #it insert value at specific position i.e the 1st num is postion the second will value

num.remove(3)   #remove specific value

num.pop()   #remove last value

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
l7 = [i*i for i in l6]      # 1,4,9,36.........

import collections


from collections import Counter
# list comprehension

l5 = [1,2,3,4,5,6,7,8]
l6 = [i*i for i in l5 if i==3 or i == 5]
print(l6)

# how to count numbers in the array
a = 'kkkffffffffhhhhhhhhs';

char_in_dict = {}

for char in a:
    if char in char_in_dict:
        char_in_dict[char] +=1 
    else:
        char_in_dict[char] = 1

print(char_in_dict)

b = Counter(a)
print(b)


# how to remove duplicaaes without changing their position

# how to remove duplicattrs number from list
a = [5,7,8,1,2,3,5,7,8,4,3,5,6,7]

b = set(a)

z = list(b)
print(b)
print(a)
print(z)


# how to remove duplicaaes without changing their position

a = [5,7,8,1,2,3,5,7,8,4,3,5,6,7]

b = set(a)

a = [5,7,8,1,2,3,5,7,8,4,3,5,6,7]
c = set()
unique_list = []

for i in a:
    if i  not in c:
        unique_list.append(i)
        c.add(i)

print(unique_list)

# 
print("How would you merge two sorted lists into a single sorted list?")

s1 = [1,3,4,5,7]
s2 = [0,1,2,4,5,7,8]
s3 = []

print(s1)
print(s2)
s1 = [1, 3, 4, 5, 7]
s2 = [0, 1, 2, 4, 5, 7, 8]
s3 = []

i, j = 0, 0  # Pointers for s1 and s2

while i < len(s1) and j < len(s2):
    if s1[i] < s2[j]:
        s3.append(s1[i])
        i += 1
    else:
        s3.append(s2[j])
        j += 1

# Append remaining elements if any
s3.extend(s1[i:])
s3.extend(s2[j:])

print(s3)


# ///////////////Max and Min
l1  =[98,5,4,33,66,11,44,101,455,333]

# a= max(l1) b = min(l1)

i = 0
j = 1
max = l1[0]
for i in range(len(l1)):
    if max < l1[i]:
        max = l1[i]

print(max)

min = l1[0]
for i in range(len(l1)):
    if min > l1[i]:
        min = l1[i]
print(min)


d1 = {}
d2 = dict()

d1 = {"name":"rahim"}
d2 = {"age":"23"}
d1.update(d2)
print(d1)
print(d2)

# how to iterate over dictionary
for keys,values in d1.items():
    print(keys,values)

# merging two dictionaries

d1.update(d2)

d3 = {**d1, **d2}

# how to remove data from a dictionary
# del d3["age"]
d3.pop("name")
print(d3)

# to check existance of key

if "age" in d3:
    print("age of Rahim: ", d3["age"])


# Dictionary comprehension

# how ot find  frequency of word
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

fequency_of_items = {item: elements.count(item) for item in elements}

print(fequency_of_items)


# Example 6: Combining Two Lists into a Dictionary

keys = ["1","2", "3","4","5","6"]
values = ["a","b","c","d","f","g"]

combined_list_as_dict = {keys[i]:values[i] for i in range(len(keys))}

print(combined_list_as_dict)