try:
    pi = 3.14
    radius = float(input("Enter the radius of circle....."))
    area = pi*radius**2
    circumference = 2*pi*radius
except ValueError:
    print("Please enter the valid credential...")
    print("Please Try again...")
#i am printing the result of circle
print("Area is circle :  ",area)
print("Circumference is : ",circumference)