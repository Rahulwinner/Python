try:
    num1 = float(input("enter the first number : ...."))
    num2 = float(input("enter the second number : ...."))
except:
    print("Please enter the valid credential...")
#this is my second blocks
try:
    addition = num1 + num2
    substract = num1 - num2
    multiplication = num1*num2
    division = num1/num2
    print("total is :  ",addition)
    print("substract is : ",substract)
    print("multiplication is : ",multiplication)
    print("division is : ",division)
except:
    print("Try again...")