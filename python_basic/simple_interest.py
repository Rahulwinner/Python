try:
    printcipal_amount = float(input("Enter the principal amount..."))
    time_period = int(input("Enter the tenure in month..."))
    interest = float(input("Enter the yearly interest..."))
except:
    print("Please input valid credential")
try:
    time_period = time_period/12
    simple_interest_is = (printcipal_amount*time_period*interest)/100
    print("Interest is : ",simple_interest_is)
except:
    print("please continue...")