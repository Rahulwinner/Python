try:
    fahrenheit = float(input("enter the value in Fahrenheit....."))
except:
    print("Please input a valid credential...")
try:
    celcius = (fahrenheit-32)*5/9
    print("Celcius is :  ",celcius)
except:
    print("Try again")