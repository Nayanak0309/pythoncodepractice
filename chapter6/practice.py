#write a pgm to find the greatest of 4 numbers enterd by the user
"""n1=int(input("enter the number "))
n2=int(input("enter the number "))
n3=int(input("enter the number "))
n4=int(input("enter the number "))

if(n1>=n2 and n1>=n3 and n1>=n4):
    print(n1,"n1 is greatest")
elif(n2>=n3 and n2>=n4):
    print(n2,"n2 is greatest")
elif(n3>=n4):
    print(n3,"n3 is greatest")
else:
    print(n4,"n4 is greatest")"""

#Write a program to find out whether a student has passed or failed if it requires a 
#total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#take marks as an input from the user.

"""marks1=int(input("enter the marks 1 "))
marks2=int(input("enter the marks2 "))
marks3=int(input("enter the marks 3 "))

total_per=(100*(marks1+marks2+marks3))/300

if(total_per>=40 and marks1>33 and marks2>33 and marks3>33):
    print("you are pass")
else:
    print("failed try again")"""

#A spam comment is defined as a text containing following keywords:
"""p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("enter the msg")
if((p1 in message)or (p2 in message)or(p3 in message)or(p4 in message)):
    print("the comment is spam")
else:
    print("the comment is not spam")"""

#Write a program to find whether a given username contains less than 10 
#characters or not. 
"""name=input("enter the name of the user ")
if(len(name)<10):
    print("your usernamre is less than 10")
else:
    print("all is well")"""

# Write a program which finds out whether a given name is present in a list or not. 
"""list=["nayna","raski","rashmi","bindu"]
name=input("enter the name")

if(name in list):
    print("the name in the list is exist")
else:
    print("not exist")"""

# Write a program to calculate the grade of a student from his marks from the 

"""marks=int(input("enter the marks"))
if(90<marks and marks<100):
    print("excalent") 
elif(marks>80 and marks<90):
    print("A grade")
elif(marks>70 and marks<80):
    print("B garde") 
elif(marks>60 and marks<70): 
    print("C garde") 
elif(marks>50 and marks<60): 
    print("D grade")

else:
    print("F")     """

#Write a program to find out whether a given post is talking about “Harry” or not. 
"""post=input("enter the post: ")   
if("Harry".lower() in post.lower()): #it will convert it into lower case
    print("this post is about harry")
else:
    print("this post is not about harry")"""


