#Ques6- rename a file using python file

# create a new file paste content into it and delete the old file

with open("old.txt") as f:
    content= f.read()
with open("new.txt", "w") as f:
    f.write(content)