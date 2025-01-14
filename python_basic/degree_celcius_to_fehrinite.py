try:
    celcius = float(input("Enter the value in celcius....."))
except:
    print("Please input valid credential....")
try:
    fahrenheit = (celcius*9/5)+32
    print("Fahrenheit =  ",fahrenheit)
except:
    print("continue")