class employee:
    lang = "English"
    salary = "20000"  #both of these are class attributes

    def __init__(self, name): #this is dunder method which is automatically called
        print("im not called")
        self.name=name


    def getInfo(self):
        print(f"Hi my name is {self.name}. I speak {self.lang} and earn {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning pineapple, looking  very good very niceeee")

harsh=employee("harsh")
harsh.name= "Harsh Khan"
# print(harsh.lang, harsh.salary, harsh.name)
harsh.getInfo()
harsh.greet()

will=employee("will")
will.getInfo()
smith=employee("smith")
smith.getInfo()



# here, language and salary are class attributes
# as they directly belong to the class
# where as name is an instance attribute (object attribute)

# instance attribute take preference over class attributes during assignment and retrieval
 