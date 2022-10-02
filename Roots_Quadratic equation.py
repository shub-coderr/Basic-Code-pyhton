import math

a = float(input("Enter the a\n"))
b = float(input("Enter the b\n"))
c = float(input("Enter the c\n"))
d = b ** 2 - 4 * a * c
if d == 0:
    print("Roots are equal")
    r1 = -b / 2*a
    print("Root1 = ", r1)
elif d > 0:
    print("Roots are distinct")
    r1 = -b + math.sqrt(d)/2*a
    r2 = -b - math.sqrt(d)/2*a
    print("Root1 = ", r1)
    print("Root2 = ", r2)
else:
    print("Roots are imaginary")

