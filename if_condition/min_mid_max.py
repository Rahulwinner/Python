try:
    num1 = int(input("Enter the first NO..."))
    num2 = int(input("Enter the second NO..."))
    num3 = int(input("Enter the third NO..."))
except:
    print("Please input invalid credential..")
#find the max min mid number
try:
    max_number = 0
    mid_number = 0
    min_number = 0
    if num1>num2 and num1>num3:
        max_number = num1
        if num2>num3:
            mid_number = num2
            min_number = num3 
        else:
            mid_number = num3
            min_number = num2
    elif num2>num1 and num2>num3:
        max_number = num2
        if num1>num3:
            mid_number = num1
            min_number = num3
        else:
            mid_number = num3
            min_number = num1
        
    elif num3>num1 and num3>num2:
        max_number = num3
        if num1>num2:
            mid_number = num1
            min_number = num2
        else:
            mid_number = num2
            min_number = num1
except:
    print("Try again")
#print the result 
try:
    print("max number is ",max_number)
    print("middle number is ",mid_number)
    print("min number is ",min_number)
except:
    print("Something is wrong...")
