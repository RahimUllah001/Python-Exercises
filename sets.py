# set: mutable, unordered, and collection daatatype, no duplicate


s = set("hello")
print(s)        #{'o', 'e', 'l', 'h'} means order is not important and show the 'l' only once
s = {}

s1 = set()
s1.add(0)       #adding elemnt
s1.add(1)       #adding elemnt
s1.add(2)       #adding elemnt
s1.add(3)       #adding elemnt

s1.remove(0)
print(type(s))      #type = dict
print(type(s1))      #type = set
# print(s1)    #typ

# s1.discard(3)       #if not found the not give give any error
# s1.clear()      #clear the set

# s1.pop()        #it deletes the ist and return it



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# UNION AND INTESRSECTION 
odd = {1,3,5,7,9}
even = {0,2,4,6,8}
prime ={2,3,5,7,11}

u= odd.union(even)
n = prime.intersection(odd)
print(u)
print(n)


diff = prime.difference(odd)
print(diff)

diffsymtric = prime.symmetric_difference(odd)

print(diffsymtric)      #will give all the element sof both sets except the common one

setA = {1,2,3,4,5,6}
setB = { 7,8,9,0}

setA.update(setB)

print(setA)
print(setA.issubset(setB))# false
print(setA.issuperset(setB))# true
print(setB.issubset(setA))#true
print(setB.isdisjoint(setA))#false

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# copying set is same as in list



# //////////////////////////////////////////
# frozen set is  immutable version of set

a = frozenset([1,2,3,4,5])

a.add(6)        #frozen object has no attribute add
a.remove(6)        #frozen object has no attribute add