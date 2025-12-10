#1. Write a program to print multiplication table of a given number using for loop.
"""n=int(input("enter the number"))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}") """

#2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 
"""l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")"""

#3. Attempt problem 1 using while loop. 
"""n=int(input("enter the no "))
i=0
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i +=1"""

#4. Write a program to find whether a given number is prime or not. 
"""n=int(input("enter the no "))
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("its prime no")"""

#Write a program to find the sum of first n natural numbers using while loop.
"""n=int(input("enter the number"))
i=1
sum=0
while(i<=n):
    sum += i
    i+=1
print(sum)"""


# Write a program to calculate the factorial of a given number using for loop. 
"""n=int(input("enter the no "))
product = 1  #for multification always start with 1
for i in range(1,n+1):
    product=product*i
print(f"the factorial of {n} is {product}")"""

# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 explaination i is space whrer i-n means space n is * to print the star we need the i=1 than 2*1-1=1 than it will print 1 star and so on
"""n=int(input("enter the no "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print()"""

#8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3
"""n=int(input("enter the no "))
for i in range(1,n+1):
    print("*"* i,end=" ")
    print()"""

# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *
"""n=int(input("enter the no "))
for i in range(1,n+1):
        if(i==1 or i==n):
            print("*"* n)
        else:
            print("*",end="")
            print(" "*(n-2),end="")
            print("*", end="")
            print()"""