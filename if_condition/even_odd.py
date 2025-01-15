try:
    user_input = int(input("please input the integer number..."))
except:
    print("Please enter the valid credential...")
#this is my second block
try:
    if user_input%2==0:
        print("this is even number")
    else:
        print("this is odd number")
except:
    pass