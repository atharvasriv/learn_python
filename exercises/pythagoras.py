import math as mt

print("Follows the standard convention of a²+b²=c²")

a = float(input("Please enter the length of side a: "))
b = float(input("Please enter the length of side b: "))

c = mt.sqrt(pow(a, 2) + pow(b, 2))

print(f"The length of side c is: {round(c, 2)}")
