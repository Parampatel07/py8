# Example of default argument function 
# Write a programe to findout area of cylinder 

def areaOfCylider(height,radius,pi=3.141592):
     print("The value of pi is " , pi )
     area = (2 * pi * radius * height) + (2 * pi * radius * radius)
     return area 


height = int(input("Enter value of height "))
radius = int(input("Enter value of radius "))
area = areaOfCylider(height,radius,(22/7))
print("The area of cylinder is " , area)