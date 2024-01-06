# dictioanry store information in key value pair,unordered and immutable
months = {"ist" : "jan",
          "sec": "feb"}

print(months)
print(months.get("sec"))

print(months.get("third", "not presesnt"))


dict1 = dict(name = "rahim", age = "4")     #{'age': '4'}
print(dict1)

print(dict1["age"])     #4

# del dict1["age"]        #will delete this

# dict1.pop("age")        #will remove spcific
# dict1.popitem()     # will remove last one

if "name " in dict1:
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