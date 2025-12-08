#if- else
a=int(input("enter the age "))
if(a>=18):
    print("your are eligible")
elif(a<0):
    print("invalid")
elif(a==0):
    print("age is 0 invalid")
else:
    print("not eleigible")
