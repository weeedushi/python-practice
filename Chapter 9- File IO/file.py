f= open("myText.txt")
# data= f.read()
# print(data)

line= f.readline()
while (line!=""):
    print(line)
    line=f.readline()
f.close()
