try:
    choice = input("Enter your choice (p/c)...")
    if choice =='p' or choice =='P':
        print("You like pepsi")
    elif choice=='c' or choice=='C':
        print("You like cock")
    else:
        print("Please choose p/c")
except:
    print("Please enter valid credential")