'''
1  snake
-1 water
0  gun
'''

import random

computer = random.choice([-1, 0, 1])
yourValue = input("enter your choice (s, w, g): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"} #for print statement in line 15

choice = youDict[yourValue]
print(f"computer chose {reverseDict[computer]} and you chose {reverseDict[choice]}")

if(computer==choice):
    print("draw")
else:
    if(computer ==-1 and choice==1):
        print("You win")
    elif(computer ==-1 and choice==0):
        print("You lose")
    elif(computer ==1 and choice==-1):
        print("you lose")
    elif(computer ==1 and choice==0):
        print("you win")
    elif(computer ==0 and choice==-1):
        print("you win")
    elif(computer ==0 and choice==1):
        print("you lose")
    else:
        print("something went wrong")


# WE CAN ALSO DO THIS 

# if(computer-choice==2 or computer-choice==-1):
#     print("you lose")
# else:
#     print("you win")