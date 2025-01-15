import math
try:
    side = float(input("Enter the side of cube..."))
except:
    print("Please input valid credential....")
#this is second section
try:
    total_area_of_cube = 6*(side**2)
    volume_of_cube = side**3
    diagonal_of_cube = (math.sqrt(3))*side
    lateral_surface_area = 4*(side**2)
    print("Total area of cube is : ",total_area_of_cube)
    print("Volume of cube is : ",volume_of_cube)
    print("Diagonal of cube is : ",diagonal_of_cube)
    print("lateral surface area is : ",lateral_surface_area)
except:
    print("Try again...")