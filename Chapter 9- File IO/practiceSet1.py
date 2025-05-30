#Ques1- read from a file name poem.txt
# and see check whether it contains the word "twinkle"

f=open("poem.txt")
content= f.read()
if("twinkle" in content.lower()):
    print("twinkle is there")
else:
    print("no twinkle")
f.close()