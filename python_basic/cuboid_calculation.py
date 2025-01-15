import math
try:
    length = float(input("Enter the length of cube..."))
    base = float(input("Enter the base of cube..."))
    height = float(input("Enter the height of cube..."))
except:
    print("Please enter valid credential...")
try:
    volume_of_cuboid = length*base*height
    total_area_of_cuboid = 2*(length*base+base*height+height*length)
    area_of_cuboid = 2*(length+base)*height
    diagonal_of_cuboid  = math.sqrt(length*length+base*base+height*height)
    #i am printing the result of the cuboid
    print("total area is :  ",total_area_of_cuboid)
    print("Area is : ",area_of_cuboid)
    print("Volume is : ",volume_of_cuboid)
    print("Diagonal is : ",diagonal_of_cuboid)
except NameError:
    print("Try Again....")
 