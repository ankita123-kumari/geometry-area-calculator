import math

base=float(input("enter base of triangle"))

height=float(input("enter height of triangle"))

side=float(input("enter side of equilateral triangle"))

area_of_triangle = (1/2)*(base*height)

area_of_equilateral= (math.sqrt(3)/4)*(side**2)

print(f"area of triangle {area_of_triangle}")

print(f"area of equilateral triangle {area_of_equilateral}")