a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
c=input("What do you want:- ")
if c=="+" or c=="addition":
    sum(a,b)
elif c=="-" or c=="substraction":
    sub(a,b)
elif c=="*" or c=="multiplication":
    mul(a,b)
else:
    div(a,b)
