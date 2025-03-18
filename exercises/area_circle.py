import math as mt

pi = mt.pi

radius = float(input("Please enter the radius of the circle: "))
rad2 = pow(radius, 2)
area = pi * rad2

print(f"The area of the circle is {round(area, 2)}unit²")
