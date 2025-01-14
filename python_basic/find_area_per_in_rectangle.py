try:
    length = float(input("Enter the length of rectangle...."))
    base = float(input("Enter the base of rectangle...."))
except:
    print("Invalid input")
#this is my second blocks
try:
    area = length*base
    perameter = 2*(length+base)
    print("Area is:  ",area)
    print("Perameter is: ",perameter)
except:
    print("Try again...")