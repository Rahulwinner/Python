try:
    month_number = int(input("Enter the month digit (1-12)..."))
    if month_number == 1:
        print("January 31days")
    elif month_number ==2:
        print("Februrary 28/29days")
    elif month_number ==3:
        print("March 31days")
    elif month_number ==4:
        print("April 30days")
    elif month_number ==5:
        print("May 31days")
    elif month_number ==6:
        print("June 30days")
    elif month_number ==7:
        print("July 31days")
    elif month_number ==8:
        print("August 31days")
    elif month_number ==9:
        print("September 30days")
    elif month_number ==10:
        print("October 31days")
    elif month_number ==11:
        print("November 30days")
    elif month_number ==12:
        print("December 31days")   
except:
    print("Please input valid credential..")