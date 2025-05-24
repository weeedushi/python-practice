#Ques1- WAP to print multiplication of a number

num= int(input("enter the number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

#Ques2- WAP to greet only person whose name starts with 's

l=["vidushi", "sneha", "sarthak", "praharsh", "sanchi"]
for i in l:
    if(i.startswith("s")):
        print(f"Hello {i}")
    else:
        print("no hello for you")

#Ques3 WAP to find whether a number is prime or not

n=int(input("enter the number: "))
for i in range(2,n):
    if(n%i) ==0:
        print("number is not prime")
        break
else:
    print("number is prime")

#Ques4 WAP to find sum of n natural numbers using while loop

N= int(input("enter the number: "))

sum=0
count=1
while(count<=N):
    sum=sum+count
    count+=1
print(sum)

#Ques5 WAP to find factorial of a number

n1 = int(input("enter the number: "))
fact=1
for i in range(2,n1+1):
    fact=fact*i
print(f"factorial of {n1} is {fact}")

#Ques6- printing a star pattern

"""
* * *
*   *
* * *

for n=3
"""

x= int(input("enter the number: "))
for i in range(1,x+1):
    if(i==1 or i==x):
        print("*"*x,end="")
    else:
        print("*", end="")
        print(" "*(x-2), end="")
        print("*",end="")
    print("")
