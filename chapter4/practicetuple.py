#Create a tuple with the elements: 10, 20, 30, 40, 50. Print the tuple.
"""a=(10,20,30,40,50)
print(a)"""


#Access the first and last elements of the tuple (5, 10, 15, 20).
"""my_tuple = (5, 10, 15, 20)

first_element = my_tuple[0]
last_element = my_tuple[-1]

print("First element:", first_element)
print("Last element:", last_element)"""


#Create a tuple with a single element 100. Check its type.
"""a=(100,)
print(type(a))"""

#Count how many times the number 2 appears in the tuple (1, 2, 3, 2, 4, 2) using a tuple method.
"""a=(1, 2, 3, 2, 4, 2)
print(a.count(2))"""

#Find the index of "apple" in the tuple ("orange", "apple", "banana").
"""a=("orange", "apple", "banana")
print(a.index("apple"))"""



#Intermediate Questions
#Convert the tuple (1, 2, 3, 4, 5) into a list and append 6 to it.
"""a=(1, 2, 3, 4, 5)
lists=list(a)
lists.append(6)
print(lists)"""

#Convert the tuple ("a", "b", "c") into a list, change "b" to "z", and convert it back to a tuple.
"""a=("a", "b", "c")
b=list(a)
b[1]='z'   #to replace the word we use the index
d=tuple(b)
print(d)"""


#Slice the tuple (10, 20, 30, 40, 50) to get (20, 30, 40).
"""a=(10, 20, 30, 40, 50)
b=a[1:4]  #for slicing we use the index
print(b)"""

#Combine two tuples (1, 2, 3) and (4, 5, 6) into a single tuple.
"""a=(1,2,3)
b=(4,5,6)
c=a+b
print(c)
"""

#Unpack the tuple (100, 200, 300) into three variables and print them.
"""a=(100,200,300)
b=a[0]
c=a[1]
d=a[2]
print(a)
print(b)
print(c)
print(d)"""
#or
"""a = (100, 200, 300)

b, c, d = a  # Unpack in a single line

print(a)
print(b)
print(c)
print(d)"""


#Advanced Questions

#Given a tuple of numbers (5, 10, 15, 20, 25), convert it to a list, remove all numbers greater than 15, and convert it back to a tuple.
"""a=(5, 10, 15, 20, 25)
b=list(a)
filter_list = [num for num in b if num<=15 ]
tuples=tuple(filter_list)
print(tuples)"""

#Count how many times each element appears in the tuple ("apple", "banana", "apple", "cherry", "banana", "apple"). (Hint: use a loop or a dictionary)
"""a=("apple", "banana", "apple", "cherry", "banana", "apple")
empty_dict={}
for item in a:
    if item in empty_dict:
        empty_dict[item]+=1
    else:
        empty_dict[item]=1
print(empty_dict)"""



#Given the tuple (1, (2, 3), 4, (5, 6)), access the number 6.
"""a=(1, (2, 3), 4, (5, 6))
print(a[3][1])"""

#Reverse the tuple (10, 20, 30, 40, 50) without converting it to a list.
"""og_tuple=(10, 20, 30, 40, 50)
rever_tuple=og_tuple[::-1]
print(rever_tuple)"""

#Write a program to take input from the user, split it by commas, and store it as a tuple of integers.



#write a program to store seven fruites in a list entered u the user
"""fruits=[]
f1=input("enter the fruit")
fruits.append(f1)
f2=input("enter the fruit")
fruits.append(f2)
f3=input("enter the fruit")
fruits.append(f3)
f4=input("enter the fruit")
fruits.append(f4)
f5=input("enter the fruit")
fruits.append(f5)
f6=input("enter the fruit")
fruits.append(f6)
print(fruits)"""

#write the program to accept marks of 6 students and display them in a sorted manner
"""marks=[]
f1=int(input("enter themarks"))
marks.append(f1)
f2=int(input("enter themarks"))
marks.append(f2)
f3=int(input("enter the marks "))
marks.append(f3)
f4=int(input("enter the marks"))
marks.append(f4)
f5=int(input("enter themarks"))
marks.append(f5)
f6=int(input("enter the marks"))
marks.append(f6)
marks.sort()
print(marks)"""

#check that a tuple cannot be changed in python
"""a=(32,56,"nayu")
a[2]=45"""
#cannot change the value


#write the program to sum a list with 4 numbers
"""list=[34,67,43,23]
print(sum(list))"""

#write the program to count the number of zeros in the following tuple
a=(7,0,8,0,0,9)
print(a.count(0))
