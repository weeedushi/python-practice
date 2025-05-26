def avg():
    a= int(input("enter a number: "))
    b= int(input("enter a number: "))
    c= int(input("enter a number: "))

    average = int((a+b+c)/3)
    print(average)

#factorial of a number

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        print(f"{n}*fact({n-1})")
        return n*fact(n-1)

a= fact(6)
print(a)