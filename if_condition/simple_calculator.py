try:
    print("Main menu...")
    print("1. Addition...")
    print("2. Substraction...")
    print("3. multiplication...")
    print("4. division...")
    print("5 exit...")
    choice = int(input("Enter the choice..."))
    if choice>0 and choice<6:
        num1 = float(input("Enter the first NO.."))
        num2 = float(input("Enter the second NO.."))
    if choice ==1:
        result = num1+num2
        print("Total is : ",result)
    elif choice == 2:
        result = num1-num2
        print("substraction is : ",result)
    elif choice == 3:
        result = num1*num2        
        print("multiplicatiion is : ",result)
    elif choice == 4:
        result = num1/num2
        print("division is : ",result)
    elif choice == 5:
        quit()
    else:
        print("Please input 1-5")
except:
    print("Please input valid credential..")