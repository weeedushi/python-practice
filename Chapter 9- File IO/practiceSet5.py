#Ques5- mine a log file and find out whether it contains "python" and on which line

with open("log.txt") as f:
    lines = f.readlines()

lineno=1

for line in lines:
    if("python" in line):
        print(f"yes python is present on line {lineno}")
        break
    lineno+=1

else:
    print("no python is not present")