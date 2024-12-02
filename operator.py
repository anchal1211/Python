# Assignment operators demonstration
x = 10  # Simple assignment
print("Initial value of x:", x)

x += 5  # Equivalent to x = x + 5
print("After x += 5:", x)

x -= 3  # Equivalent to x = x - 3
print("After x -= 3:", x)

x *= 2  # Equivalent to x = x * 2
print("After x *= 2:", x)

x /= 4  # Equivalent to x = x / 4
print("After x /= 4:", x)

x %= 3  # Equivalent to x = x % 3
print("After x %= 3:", x)

x **= 2  # Equivalent to x = x ** 2
print("After x **= 2:", x)

x //= 2  # Equivalent to x = x // 2
print("After x //= 2:", x)

a = 10
b = 3

print("Addition:", a + b)  # Adds two numbers
print("Subtraction:", a - b)  # Subtracts two numbers
print("Multiplication:", a * b)  # Multiplies two numbers
print("Division:", a / b)  # Divides two numbers (float result)
print("Modulus:", a % b)  # Remainder of the division
print("Exponentiation:", a ** b)  # Raises a to the power of b
print("Floor Division:", a // b)  # Divides and returns the integer part

x = True
y = False

print("Logical AND:", x and y)  # Both need to be True
print("Logical OR:", x or y)  # One needs to be True
print("Logical NOT:", not x)  # Reverses the boolean value

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Checks if 3 is in the list
print(6 not in my_list)  # Checks if 6 is not in the list

import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area_of_circle(radius))

def area_of_triangle(base, height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print("Area of the triangle:", area_of_triangle(base, height))

def area_of_rectangle(length, width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of the rectangle:", area_of_rectangle(length, width))

def area_of_square(side):
    return side ** 2

side = float(input("Enter the side of the square: "))
print("Area of the square:", area_of_square(side))

