#Ques4- A file contains a word "Donkey" multiple times
# Replace this word with ###### by updating the same file

word="donkey"

with open("myText.txt", "r") as f:
    content = f.read()

contentNew = content.lower().replace(word,"######")

with open("myText.txt", "w") as f:
    f.write(contentNew)