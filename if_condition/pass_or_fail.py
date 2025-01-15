try:
    math = float(input("Enter the math marks..."))
    sci = float(input("Enter the science marks..."))
    english = float(input("Enter the english marks..."))
    sst = float(input("Enter the social science marks..."))
    hindi = float(input("Enter the hindi marks..."))
except:
    print("Please input valid credential... ")
#this is my second section for result
try:
    total_marks = math+sci+english+sst+hindi
    percentage = total_marks/5
except:
    print("Try again...")
#this is my third block for pass or failed result
try:
    if math>32 and sci>32 and english>32 and sst>32 and hindi>32:
        print("your are passed....")
        print("Total Marks : ",total_marks)
        print("Percentage is : ",percentage)
        if percentage>=33 and percentage<50:
            print("your division : 3rd")
        elif percentage>=50 and percentage<60:
            print("your division :  2nd")
        elif percentage>=60 and percentage<=100:
            print("your division :  1st")
        
    else:
        print("your are failed....")
        print("Total Marks : ",total_marks)
        print("Percentage is : ",percentage)
        
except:
    print("Something is wrong....")
