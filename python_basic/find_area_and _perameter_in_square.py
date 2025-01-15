try:
    side = float(input("Enter the side of square "))
    area = side**2
    perameter = 4*side
except ValueError:
    print("Please enter the valid credential....")
    print("Try again ....")
#print the result
print("Area is square :  ",area)
print("Perameter is square : ",perameter)
    