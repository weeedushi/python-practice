student={
    "name":"vidushi",
    "age":20,
    "sex":"F",
    "name":"sneha"
}

print(student)

#Ques1- WAP to create a hindi dictionary with values as english translation and give users the option to look it up

dict={
    "fool":"flower",
    "vichitra":"peculiar",
    "alag":"different"
}
print(dict.keys())
userI=input("enter word: ")
print(dict.get(userI))

#Ques2- WAP to input six numbers from user and display all the unique numbers all at once
sets=set()
no1=int(input("enter number 1: "))
sets.add(no1)
no2=int(input("enter number 2: "))
sets.add(no2)
no3=int(input("enter number 3: "))
sets.add(no3)
no4=int(input("enter number 4: "))
sets.add(no4)
no5=int(input("enter number 5: "))
sets.add(no5)
no6=int(input("enter number 6: "))
sets.add(no6)

print(sets)

#Ques3- Create an empty dictionary. ALlow four friends to enter their favorite language as value and use key as their names. Assume that the names are unique

d={}
name =input("enter friends name: ")
lang=input("enter language name: ")
d.update({name: lang})

name =input("enter friends name: ")
lang=input("enter language name: ")
d.update({name: lang})

name =input("enter friends name: ")
lang=input("enter language name: ")
d.update({name: lang})

name =input("enter friends name: ")
lang=input("enter language name: ")
d.update({name: lang})

print(d)


