# Input sides, check for triangle validity, and classify (equilateral, isosceles, scalene).
# equilateral - all three sides length are equal(a == b == c)
# isosceles triangle - any two side of triangle are equal(a==b or a==c or b==c )
# scalene triangle - all three side's are different

side_1 = float(input("enter the value of first side: "))
side_2 = float(input("enter the value of second side: "))
side_3 = float(input("enter the value of third side: "))
if side_1 > 0 and side_2 > 0 and side_3 > 0 and \
   side_1 + side_2 > side_3 and \
   side_1 + side_3 > side_2 and \
   side_2 + side_3 > side_1:
    # # Equilateral triangle (only possible when all angles are 60)
    if side_1 == side_2 == side_3 == 60:
        print("the triangle are equilateral")
# isosceles triangle
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("the triangle are isosceles")
    # scalene triangle
    else:
        print("the triangle are scalene triangle ")
else:
    print("The given sides do not form a triangle.")
