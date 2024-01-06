# string ordered, immutable text representation
print("python \"develper")    # how to print quotation mark in python

my_profession = "Web Development"

print(my_profession.lower()) # to make all character small
print(my_profession.upper()) # to make all character capitale

print(my_profession.isupper()) # to check all the character are capital or not -->Result False B/C  strings are immutable in python until i not 
# reassign the the new value to the variable it will not change and when we reassin the new value to the same variable the previuos value 
# is still store in the memory but the variable is now assign to the new value
my_profession = my_profession.upper()
print(my_profession.isupper()) # now it will give expected result i.e True

name = "Rahim"
print(id(name)) #memory address

print(len(my_profession)) #the length of the string

print(my_profession[0])  # to take the individual character
my_profession = "Web Development"

print(my_profession.index("l"))  # to find the index of character i.e 8

print( my_profession.replace("Web","App")) #to replace xxxxx
mystring = """ hello   
    world"""

print(mystring)     #hello and world in new line
mystring1 = """                 hello   \
    world"""

print(mystring1)        # hello         world



# /////////////////////////////////////////////////////////////////////
# string also  supports slicing
print(mystring1.strip())    #can remove the extra space in start and after

# .startwith and .endswith  checks the start and last

# .find use to find the index of any character 

mylist = mystring.split() # string to list
print(mylist)       #['hello','world']
newstring = ' '.join(mylist)
print(newstring)        #hello world
