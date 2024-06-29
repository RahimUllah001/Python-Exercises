from tuples import key

# dictioanry store information in key value pair,unordered and immutable
months = {"ist" : "jan",
          "sec": "feb"}

print(months)
print(months.get("sec"))

print(months.get("third", "not presesnt"))


dict1 = dict(name = "rahim", age = "4")     #{'name': 'rahim', 'age': '4'}
print(dict1)

print(dict1["age"])     #4

# del dict1["age"]        #will delete this

# dict1.pop("age")        #will remove spcific
# dict1.popitem()     # will remove last one

if "name" in dict1:
    print(dict1["name"])



try:
    print(dict1["phone_number"])    
except:
    print("error")    

for key,values in dict1.items():
    print(key, values)      #   name rahim

# ///////////////////////////////////////////////////////////////
# copying is same as in case of list


# updating dictoionary

d1 = {"name" :"aaaaa", "age" :5}
d2 = {"name" :"rahim", "p_number": 9987}        # name will be updated and phone number will be added

d1.update(d2)

print(d1)


d3 = {3:5,6:9,8:16}
print(d3)
mytple = (8,7)

d3 = {mytple:15}
print(d3) # {(8,7):15}




# to make a dictionary of such whose value are aquare of their keys

a = [1,2,3,4,5]

d11 = {num:num*num for num in a}
print(d11)

# Example 3: Using Strings
# Creating a dictionary from a string where keys are characters and values are their ASCII values.
text = "rahim"
d11 = {keys: ord(keys) for keys in text }
print(d11)


# swapping key and values
original_dict = {'a': 1, 'b': 2, 'c': 3}

new_dict = {value:key for key,value in original_dict.items()}
print(new_dict)