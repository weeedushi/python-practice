import math
#Ques1- Create a class "programmer" for storing info of few prograamers working at microsoft

class programmers:
    company = "Microsoft"
    def __init__(self, name, salary, lang):
        self.name= name
        self.salary= salary
        self.lang= lang
    def info(self):
        print(f"my name is {self.name}. I code in {self.lang} and earn {self.salary} in {self.company}")

vidushi=programmers("vidushi", 1000000, "python")
vidushi.info()

#Ques2- Write a class "calculator" capable of finding square, cube and square root of a number

class calculator:
    def sq(self, num):
        return num**2
    def cube(self, num):
        return num**3
    def sqrt(self, num):
        if num<0:
            raise ValueError("can't compute squre root of a negative number")
        return math.sqrt(num)

calc = calculator()
num=9
print(f"square is {calc.sq(num)}")
print(f"cube is {calc.cube(num)}")
print(f"sqrt is {calc.sqrt(num)}")


#Ques3- Create a class with a class attribute "a"; create an object from it and set a directly using object.a=0. Does this change the class attribute?

class first:
    value=4

x=first()
print(x.value)
x.value=14
print(x.value)
print(first.value)

class train:
    def tickets(self, trainNo, fro, to):
        print(f"ticket is booked in train number: {trainNo} from {fro} to {to}")
    def getStatus(self, trainNo):
        pass
    def getFare(self, trainNo, fro, to):
        pass