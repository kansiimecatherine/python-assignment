#Create a program to calculate the area of a triangle (1/2*base*height).
#Base and height should be entered using a keyboard.
          #solution
#approach one

base= int(input("Enter the base of a triangle:"))
height = int(input("Enter the height of a triangle:"))
area_of_a_triangle = ((1/2)*base*height)

print(f"The area of a triangle is :{area_of_a_triangle:}")

# # approach two
def area_of_triangle ():
    
     base= int(input("Enter the base of a triangle:"))
     height = int(input("Enter the height of a triangle:"))
     area = ((1/2)*base*height)
print(f"The area of a triangle of base {base} and height {height} is {area:}")

area_of_triangle()


#approach three
base= int(input("Enter the base of a triangle:"))
height= int(input("Enter the height of a triangle:"))

def area_of_triangle (b,h):
    area_of_triangle = (1/2) * b * h

    print(f"The area of the triangle with base{b} and height {h} is {area_of_triangle:.2f}")
area_of_triangle(base,height)



