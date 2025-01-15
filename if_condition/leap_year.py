try:
    year = int(input("Enter the year...."))
except:
    print("Please input valid crendential")
#this is my second block
try:
    if (year%4==0) and (year%100!=0) or (year%400==0):
        print("This is leap year")
    else:
        print("This is not leap year")
    
except:
    print("Try again..")