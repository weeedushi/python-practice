#Ques3- to generate multiplication tables from 2 to 20
# and write these tables into different files 
# and put these files into a folder

def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)