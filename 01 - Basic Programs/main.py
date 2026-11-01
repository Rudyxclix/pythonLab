import math

radius = float(input("Enter the radius of the circle: "))
if radius < 0:
    print("Radius cannot be negative.")
else:
    area = math.pi * radius * radius
    print("Area of the circle:", round(area, 2))

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

if first >= second and first >= third:
    largest = first
elif second >= first and second >= third:
    largest = second
else:
    largest = third

print("Largest number:", largest)