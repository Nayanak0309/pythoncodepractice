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
n=int(input("enter the number"))
i=1
sum=0
while(i<=n):
    sum += i
    i+=1
print(sum)