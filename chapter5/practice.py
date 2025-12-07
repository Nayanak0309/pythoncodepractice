#Create a dictionary of a student with keys: name, age, branch. Print all values.
"""student={"name":"nayana",
         "age":22,
         "branch":"cse",
         }
print(student)"""

#Count how many times each word appears in this list:
"""words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
dict_empt={}
for item in words:
    if item in dict_empt:
        dict_empt[item]+=1
    else:
        dict_empt[item]=1
print(dict_empt)"""

#Create a dictionary from keys ["a","b","c"] with default value 0.
"""a=["a","b","c"]
print(dict.fromkeys(a,0))"""

#Add a new key "city" to this dictionary:
"""person = {"name": "Nayana", "age": 21}
person.update({"city":"bangalore"})
print(person)"""

#Remove "age" key from the same dictionary
"""person = {"name": "Nayana", "age": 21}
person.pop("age")
print(person)"""

#Given a dictionary, print only the keys:
"""d = {"a": 1, "b": 2, "c": 3}
print(d.keys())"""

#Merge these two dictionaries using update()
"""d1 = {"name": "Nayana"}
d1.update({"age": 21, "branch": "CSE"})
print(d1)"""

#or
"""d1 = {"name": "Nayana"}
d2={"age": 21, "branch": "CSE"}
d1.update(d2)
print(d1)"""

#Create a dictionary where keys are numbers 1–5 and values are their squares
"""square={x:x*x for x in range(1,6)}
print(square)"""

#or
"""square={}
for x in range(1,6):
    square[x]=x*x

print(square)"""

#Swap keys and values of the dictionary

"""d = {"a": 1, "b": 2, "c": 3}
swapped={}
for keys,value in d.items():
    swapped[value]=keys
print(swapped)
"""
#or
"""d = {"a": 1, "b": 2, "c": 3}
swapped={values:keys for keys, values in d.items()}
print(swapped)"""

#Find the key with the maximum value
"""d = {"a": 5, "b": 9, "c": 3}
max_value=max(d,key=d.get)
print(max_value)"""

#Count character frequency of a string using dictionary.
"""a="banana"
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)"""

#Convert two lists into a dictionary
"""keys = ["name", "age", "city"]
values = ["Nayana", 21, "Bangalore"]

resulr=dict(zip(keys,values))
print(resulr)"""
#or

"""keys = ["name", "age", "city"]
values = ["Nayana", 21, "Bangalore"]
result={}
for i in range(len(keys)):
    result[keys[i]]=values[i]
print(result)"""


#write the program to create a dictionary of hindi words with valuew as eas their english translation 
"""words={
    "madad":"help",
    "billa":"cat",
    "sona":"gold"
}
word=input("enter the word you want to translate ")
print(words[word])"""

#write  aprogram to input eight number from the user and display all the uniques numbers(once)
"""s=set()
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))
n=input("enter the no ")
s.add(int(n))

print(s)
"""


#can we have a set with 18(int) and 18(string) as a value in it
s=set()
s.add(18)
s.add("18")
print(s)#possible because both are differnt datatype


#what will be the length of the following set s
"""s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)"""

#s={}what is the type of it
"""s={}
print(type(s)) #dict type
s=set()
print(s)""" #set type

#create an empty dict, allow 4 friends to enter thier fvrt lang as value and keys as their names .assume that names are uniqu
s={}

for i in range(4):

    name=input("enter the name ")
    lang=input("enter the fvrt lang ")
    s[name]=lang
print(s)    

