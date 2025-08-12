
# Input angles and check if they form a valid triangle.
angle_1 = float(input("enter the value of first angle: "))
angle_2 = float(input("enter the value of second angle: "))
angle_3 = float(input("enter the value of third angle: "))

total_of_angle = angle_1 + angle_2 + angle_3
if angle_1 > 0 and angle_2 >0 and angle_3 > 0:
    if total_of_angle == 180:
        print("the angle is valid triangle")
    else:
        print("the angle is invalid")
else:
    print("enter the valid number")