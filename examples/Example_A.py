
#Example A: Ask user to input length and breadth and find
# area and perimeter of rectangle.


"""
While taking input using "input()" function it will only take input in string data type,
so we need to convert that string data into our desired datatype,
For example:
    length = int(input("Enter length of rectangle: "))
    will convert string data type into integer

"""

length = float(input("Enter length of rectangle: "))
breadth= float(input("Enter breadth of rectangle: "))

area = length*breadth
perimeter = 2*(length + breadth)

print("The area of rectangle is: ", area)
print("The perimeter of rectangle is: ", perimeter)