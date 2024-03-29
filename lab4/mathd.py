#ex1
import math

degrees = float(input("Enter the angle in degrees: "))

radians = math.radians(degrees)

print("The angle {degrees} degrees is equal to {radians} radians.")
#ex2

height = float(input("Enter the height of the trapezoid: "))
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))

area = 0.5 * (base1 + base2) * height

print("The area of the trapezoid is: {area}")
#ex3
import math

num_sides = int(input("Enter the number of sides of the regular polygon: "))
side_length = float(input("Enter the length of each side: "))

area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

print("The area of the regular polygon is: {area}")
#ex4

base_length = float(input("Enter the length of the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = base_length * height

print("The area of the parallelogram is: {area}")

