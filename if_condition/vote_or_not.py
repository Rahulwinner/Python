try:
    user_age = int(input("enter your age..."))
except:
    print("please input valid credential")
#this is my second block
try:
    if user_age>=18:
        print("you can vote...")
    else:
        print("you cant vote because your age is less than 18")
except:
    print("Try again...")