# Ques1- Write a program to store 7 fruits in a list entered by the user

fruits = []

print(type(fruits))

f1=input("Enter fruit name: ")
fruits.append(f1)
f2=input("Enter fruit name: ")
fruits.append(f2)
f3=input("Enter fruit name: ")
fruits.append(f3)
f4=input("Enter fruit name: ")
fruits.append(f4)
f5=input("Enter fruit name: ")
fruits.append(f5)
f6=input("Enter fruit name: ")
fruits.append(f6)
f7=input("Enter fruit name: ")
fruits.append(f7)

print(fruits)

#Ques2- WAP to input marks of 6 students and display them in sorted order

marks=[]
st1=int(input("enter marks of student 1: "))
marks.append(st1)
st2=int(input("enter marks of student 2: "))
marks.append(st2)
st3=int(input("enter marks of student 3: "))
marks.append(st3)
st4=int(input("enter marks iof student 4: "))
marks.append(st4)
st5=int(input("enter marks of student 5: "))
marks.append(st5)
st6=int(input("enter marks iof student 6: "))
marks.append(st6)

marks.sort()
print(marks)
