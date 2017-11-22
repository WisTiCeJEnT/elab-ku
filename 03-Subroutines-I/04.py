from math import pi
def circle_area(r):
    return pi*r*r
def circle_circumference(r):
    return pi*r*2

x = float(input("Enter circle radius: "))
print(f"Circle circumference is {circle_circumference(x):.2f}")
print(f"Circle area is {circle_area(x):.2f}")
