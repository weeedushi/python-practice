# Ques1- WAP to print the largest of 4 numbers entered by users

a1=int(input("enter number: "))
a2=int(input("enter number: "))
a3=int(input("enter number: "))
a4=int(input("enter number: "))


if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is ",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is ",a3)
else:
    print("Greatest number is ",a4)

#Ques2- WAP to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

eng=int(input("enter english marks: "))
math=int(input("enter maths marks: "))
arts=int(input("enter arts marks: "))

percent= ((eng+math+arts)*100)/300

if(percent>40 and eng>33 and math>33 and arts>33):
    print("pass", percent)
else:
    print("fail", percent)

#Ques3- A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". WAP to detect these spams

p1="make a lot of money"
p2="click this"
p3="subscribe this"
p4="buy now"

str = input("enter your message: ")
newStr= str.lower()

if ((p1 in newStr) or (p2 in newStr) or (p3 in newStr) or (p4 in newStr)):
    print("spam")
else:
    print("okie dokie")

#Ques4- WAP to find whether a given username contains less than 10 characters or not

username= input("enter username: ")

if(len(username)<10):
    print("username contain less than 10 characters")
else:
    print("good")

# Ques5- WAP to find out whether a given name is present in a list or not

l=["vidushi", "abhishek", "tushar", "sneha", "sarthak"]

name=input("Enter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not on the list")

#Ques6- WAP to check whether a post is talking about harry or not

post = input("enter post: ")

if("Harry".lower() in post.lower()):
    print("this post is talking about Harry")
print("thanks bye")