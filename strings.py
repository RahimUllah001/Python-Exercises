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

print( my_profession.replace("Web","App")) #to replace 
mystring = """hello   
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


# revere a string

s1 = 'rahim'
s2 = s1[::-1]
print(s2)

s1 = "abdulsamad"
s2 = ''

j = len(s1)-1

while j >= 0:
    s2 += s1[j]
    j -= 1

print(s2)

# to check palindrome

sp = "karak"
j = len(sp)-1 
i = 0
while j >= 0:
    if sp[i] == sp[j]:
        j -= 1
        i += 1
    else:
        break

if i == len(sp) :
    print("palidndrome")

# easiest way of checking palindrome

if sp[::] == sp[::-1]:
    print("it is palindrome and i finde through slicing")


    # count_vowels_and_consonants("hello world")  # Output: (3, 7)

phrase = "rahim"
vow = 0
cons = 0
vowels = "aeiou"
for i in phrase:
    if i in vowels:
        vow += 1
    else:
        cons += 1

print(f"vowels = {vow} and consonants = {cons}")

# python program that remove dublicates from string
a = "applewazir"
non_duplicate = ''
for i in a:
    if i not in non_duplicate:
       non_duplicate =non_duplicate + i

print(non_duplicate)


# longest_word("The quick brown fox jumps over the lazy dog")  # Output: "jumps"
a = "The quick brown fox jumps over the lazy dog"


words = a.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)


# find the number of words in phrase

a = "The quick brown fox jumps over the lazy dog"

words = a.split()

b = len(words)
print("The number of wrods in a given phrase is ", b)

# Write a function that checks if two given strings are anagrams (contain the same characters in different order)

s1 = "sieent"
s2 = "listen"

if sorted(s1) == sorted(s2) :
    print("anagram")