import math
try:
    user_input = float(input("Please enter the number...."))
except:
    print("Please enter valid credentials")
#this is my second blocks
try:
    power = math.pow(user_input,2)
    print("square is :  ",power)
except:
    print("Try again...")
    