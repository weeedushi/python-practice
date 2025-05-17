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