import random

num=int(input("enter any number: "))
num1=random.randint(1,num)
num2=random.randint(num1,num)

sum=0
i=1

while num1>= i :
    i=i+num2
    sum=sum+i

print("sum: ", sum)