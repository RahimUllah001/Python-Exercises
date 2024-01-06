# itertolls: product,combination,permutation,accumulate, groupby and infinite itertools
# itertools are datatype that are used in a for loop
from itertools import product, permutations,combinations,combinations_with_replacement,accumulate,groupby,count,repeat,cycle
import operator

a=[1,2]
b=[3,4]

prod = product(a,b)     #[(1, 3), (1, 4), (2, 3), (2, 4)]


print(list(prod))
# ///////////////////permutation///////////////
# ///////////////////
# ///////////////////

c = [1,2,3]
print(list(permutations(c)))
print(list(permutations(c,2))) #permutation of length 2

# ///////////////////
# ///////////////////
# ///////////////////combination//////////here no repeatition is allowed

d = [1,2,3,4]

print(list(combinations(d,2)))
print(list(combinations_with_replacement(d,2)))     # means repitition allowed here

# //////////////////////////////////////////
# //////////////////////////////////////////
# //////////////////////////////////////////
# Accumuate function

acc = [1,2,3,4]
print(list(accumulate(acc)))        #[1, 3, 6, 10]this only sum
print(list(accumulate(acc,func = operator.mul)))#[1, 2, 6, 24]this will multiply
maxm = [1,2,5,3,4]
print(list(accumulate(maxm,func = max)))#[1, 2, 5, 5, 5]



# //////////////////////////////////////////
# //////////////////////////////////////////
# groupby but this concept is not clear
g = [1,2,3,4,5]

def smaller_than_3(x):
    return x<3
group_obj = groupby(g, key = smaller_than_3)

for key,value in group_obj:
    print(key,list(value)) #True [1, 2] False [3, 4, 5]



    person = [
        {"name":"rahim", "age":23},
        {"name":"rwim" ,"age":23},
        {"name":"nahim", "age":26},
        {"name":"raddddim", "age":26}]


group_by_age = groupby(person,key = lambda x:x["age"])


for key,value in group_by_age:
    print(key,list(value)) 
    '''23 [{'name': 'rahim', 'age': 23}, {'name': 'rwim', 'age': 23}]
       26 [{'name': 'nahim', 'age': 26}, {'name': 'raddddim', 'age': 26}]''' 
    
    
# //////////////////////////////////////////
# //////////////////////////////////////////
# //////////////////////////////////////////
# ///////////////////////////////      Count()             ///////////////////
    
for i in count(10):     #it will print from 10 upto 15
    print(i)
    if i==15:
        break

for i in repeat(2,4):   #repeat 2 upto four times
    print(i)

    
# //////////////////////////////////////////
# //////////////////////////////////////////
# //////////////////////////////////////////
    