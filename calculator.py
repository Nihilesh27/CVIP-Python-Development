num1=int(input("enter 1st no.:"))
num2=int(input("enter 2st no.:"))
symbol=input("enter the symbol(+-*/%):")
if symbol == "+":
    num3=num1+num2
elif symbol=="-":
    num3=num1-num2
elif symbol=="*":
    num3=num1*num2
elif symbol=="/":
    num3=num1/num2
elif symbol=="%":
    num3=num1%num2
else:
    print("select valid symbol")