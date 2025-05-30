#Ques2- save high score in a text file and update the high score when new score is made

import random
def game():
    print("you're playing the game..")
    score=random.randint(1, 62)

    #fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore= int(hiscore)
        else:
            hiscore=0


    print(f"Your score: {score}")


    if(score>hiscore or hiscore==""):
        #write this hiscore to the file
        if(score>hiscore):
            with open("hiscore.txt", "w") as f:
                f.write(str(score))

    return score

game()
