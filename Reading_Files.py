family_file = open("textfile.txt","r") #reading information
print(family_file.readable()) #we should check that the file is readable or not

# print(family_file.read()) # to read all 

# print(family_file.readline()) #to read only loine starts from ist one 

# print(family_file.readlines()[1])  #family_file.readlines() this function gives the file ion a array style so we can access the specific infomation by indexing

for data in family_file.readlines():
    print(data)



family_file.close()

family_file = open("textfile.txt","w") #overriding a file
 
# family_file.write("\nume hani")

family_file = open("textfile.txt","r+") # appending new information at the last 
print(family_file.writable()) #we should check that the file is writable or not
 
family_file.write("\nume hani")
print(family_file.read())

open("textfile.txt","r+") # read + wride information

# open("index.html","w") # in this way we can also make a mew file
# family_file.write("<p>thsi is Paragaph </p>")
