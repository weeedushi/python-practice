#Ques1- WAP to find the greatest of 3 numbers using functions

def greatestOf3(a,b,c):
    if(a>=b and a>=c):
        print(f"{a} is the greatest")
    elif(b>=a and b>=c):
        print(f"{b} is the greatest")
    elif(c>=a and c>=b):
        print(f"{c} is the greatest")

greatestOf3(15,7,45678)

#Ques2- WAP to convert celsius into farhenheit

def conversion(temp1):
    newTemp=((temp1*9/5)+32)
    print(newTemp)

temp=int(input("enter the temperature: "))
conversion(temp)

#Ques3- Write a recursive function to calculate the sum of first n natural numbers

def sumOf(n):
    if n==1:
        return 1
    else:
        return (n + sumOf(n-1))

a=sumOf(100)
print(a)

#Ques4- WAP to print multiplication table of a number using function

def multi(n):
    for i in range(0,11):
        print(f"{n}X{i}={n*i}")

num= int(input("entere the number: "))
multi(num)

#Ques5- Write a python function to print first n lines of the following pattern
"""
*****
****
***
**
*
"""
def pattern(x):
    for i in range (0,x+1):
        print("*"*(x-i))
x=int(input("enter the number of lines: "))
pattern(x)

#Ques6- Write a function to remove a given word from a list and strip it at the same time

def rem(l, word):
    n=[]
    for item in l:
        if not(item ==word):
            n.append(item.strip(word))
    return n
    
l=["Harry", "Vidushi", "Sneha", "Vedant", "shi"]

print(rem(l, "shi"))
