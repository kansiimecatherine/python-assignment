#The volume of the sphere with radius r is (4/3)*pie**2.
#What is the volume of the sphere with radius 5.Make sure
#the program enters the radius from the keyboard and 
#provide the answer in 2 decimal places.
               #solution

radius = int(input("Enter the radius of a sphere:"))#Input radius from the keyboard
pie = 22/7#This is constant value for pie
volume_of_the_sphere = (4/3)*(pie)*(radius**2)# Formula for the volume of the sphere
print(f"The volume of a sphere with radius {radius} is :{volume_of_the_sphere:.2f}")