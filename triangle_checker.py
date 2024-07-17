side1 = int(input("side 1: "))
side2 = int(input("side 2: "))
side3 = int(input("side 3: "))
#equilateral
side_sum = (side1 + side2 + side3)/2
if side1 < side_sum and side2 < side_sum and side3 < side_sum:
    print("triangle is valid")
else:
    print("triangle is invalid")
#checking what type of triangle it is
if side1 == side2 == side3:
    print("equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("isoceles")
else:
    print("scalene")
    #scalene
