# 1. Evaluate and display the result of arithmetic expressions (test integer division
# vs float division).
# num = int(input('Enter a integer number: '))
# num2 = int(input('Enter another integer number: '))
# num3 = num // num2
# print("the integer division is:", num3)
# import math
# a = float(input('Enter a float number: '))
# b = float(input('Enter a float number: '))
# c = float(input('Enter a float number: '))
# # c = a // b
# # print("the float division is:", c)
# # 2. Find the roots of a quadratic equation given coefficients a, b, and c
# root = (b * b) - 4*(a * c)
# print(root)
# root1 = math.sqrt(root)
# print(root1)
# root2 = (-(b + root1)) / (2 * a)
# print(root2)
# root3 = (-(b - root1)) / (2 * a)
# print(root3)
# value of q equation is 3, -5, 2
# 3. Read multiple types of data (int, float, str) and print them with formatted
# output.

# data1  = int(input("enter the data1:"))
# print(f"the given data is: {data1} : {type(data1)}")
#
# data  = float(input("enter the data:"))
# print(f"the given data is: {data} : {type(data)}")
#
# data2  = input("enter the data2:")
# print(f"the given data is: {data2} : {type(data2)}")
# 4. Demonstrate explicit and implicit type conversions (casting).
# explicit type conversion
# num = input("enter the  number: ")
# print(type(num)," : ", num)
# number = int(num)
# number2 = float(num)
# print(type(number),":",number)
# print(type(number2), ":",number2)
# num2 = int(input("enter the value"))
# num4 = float(num2)
# print(type(num4)," : ", num4)
# num5 = str(num2)
# print(type(num5)," : ", num5)
# num6 = str(num4)
# print(type(num6)," : ", num6)
# num7 = int(num4)
# print(type(num7)," : ", num7)
# implicit type conversions
# a = 10
# print(type(a)," : ", a)
# b = True
# print(type(b)," : ", b)
# c = a + b
# print(type(c)," : ", c)
# print(c)
# d = 10.3
# f = a + d
# print(type(f)," : ", f)
# g = a + b + d
# print(type(f)," : ", f)
#
# x = 5
# z = a / x
# print(type(z)," : ", z      )
# 1. Use escape sequences (\n, \t, \\) in print statements.

# while a < 15:
#     a += 1
#     # print(f" \n {a}")
#     # print("\t",a)
#     print("\\", a)
# 2. Print multi-line strings using triple quotes.
# print('''priya is great''')


# Use constants: declare a value as a constant by convention (ALL_CAPS) and
# demonstrate usage.
# PI = 3.14
# r = 5
# area_of_circle = PI * r * r
# print(area_of_circle)
# 2. Use enum. Enum for symbolic constants.

import enum
# 3. Input angles and check if they form a valid triangle.

# angle1  = int(input("enter the angle first"))
# angle2 = int(input("enter the second angle "))
# angle3 = int(input("enter the third angle "))
#
# total = angle1 + angle2 + angle3
# if total == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
#     print(" Input angles they form a valid triangle")
# else:
#     print(" Input angles they not form a valid triangle")
# 4. Input sides, check for triangle validity, and classify (equilateral, isosceles,
# scalene).
# side1  = int(input("enter the side first:"))
# side2  = int(input("enter the second side: "))
# side3 = int(input("enter the third side: "))
# total = side1 + side2 + side3
# if total >= 180 and side1 > 0 and side2 > 0 and side3 > 0:
#     print("give side's make the trangle and ")
#     if side1 == side2 or side1 == side3 or side2 == side3:
#         print(" the given trangle is the isosceles trangle")
#     elif side1 == side2 == side3:
#         print("the given trangle is the equilateral trangle")
#     else:
#         print("the given trangle is the scalene trangle")
# else:
#     print("please check your input")

# 5. Input the week number (1–7) and print the corresponding weekday name
# from enum import Enum
# class Week(Enum):
#        sunday = 1
#        monday = 2
#        tuesday = 3
#        wednesday = 4
#        thursday = 5
#        friday = 6
#        saturday = 7
# # print(Week.sunday)
#
# num = int(input("enter the number from 1 to 7 : "))
# if num > 0 and num < 7:
#     print(f"number is : {num}" )
#     if num == 1:
#         print("the day is SUNDAY")
#     elif num == 2:
#         print("the day is MONDAY")
#     elif num == 3:
#         print("the day is TUESDAY")
#     elif num == 4:
#         print("the day is WEDNESSDAY")
#     elif num == 5:
#         print("the day is THURSDAY")
#     elif num == 6:
#         print("the day is FRIDAY")
#     elif num == 7:
#         print("the day is SATURDAY")
#     else:
#         print("enter the valid no")
# else:
#     print("enter the integer number from 1 to 7 ")

# 6. Input a month number (1–12), display days in the month (handle leap years for February).
# Month = int(input("Enter a month number: "))
# year = int(input("Enter a year: "))
#
# if Month in [1,3,5,7,8,10,12]:
#         print("31 day's in Month")
# elif Month == 2:
#         if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
#             print("29 day's in Month")
#         else:
#             print("28 day's in Month")
# elif Month in [4,6,9,11]:
#     print("30 day's in Month")

# 1. Simple calculator using match-case for operations (+, -, *, /).

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# op = input("enter the operator:")
# match op:
#     case "+":
#         print(f"The sum of {num1} and {num2} is {num1 + num2}")
#     case "*":
#         print(f"The product of {num1} and {num2} is {num1 * num2}")
#     case "-":
#         print(f"The difference of {num1} and {num2} is {num1 - num2}")
#     case "/":
#         print(f"The quotient of {num1} and {num2} is {num1 / num2}")

# 2. Print weekday based on user number input using match-case.
# num = int(input("enter the number from : "))
# match num:
#     case 1:
#         print("the day is sunday")
#     case 2:
#         print("the day is monday")
#     case 3:
#         print("the day is tuesday")
#     case 4:
#         print("the day is the wednesday")
#     case 5:
#         print("the day is thursday")
#     case 6:
#         print("the day is friday")
#     case 7:
#         print(" the day is the saturday")
# 3. Input grade character and print remarks using match-case.
# grade = input("Enter your grade: ")
# match grade:
#     case "A":
#         print("this is very good grade")
#     case "B":
#         print("this is good grade")
#     case "c":
#         print("this is not good grade")
# 4. Handle out-of-range input with a default message.
# msg = input("Enter message: ")
# match msg:
#     case "hello":
#         print("Hello, World!")
#     case "hi":
#         print("Goodby , World!")
#     case _:
#         print("Sorry, I don't understand.")
# 1. Use escape sequences (\n, \t, \\) in print statements.


# while i < 10:
#     print("value of I:\n",i)
#     i += 1
# for i in range(0,11):
#     # print("value of each for is: ",i)
#     # if (i % 2 ==0):
#     #     print("value of each for is: \t", i)
#     if (i % 2 ==0):
#         i += 2
#         print("value of each for is: \\",'*')
# 2. Print multi-line strings using triple quotes.
# print('''priyanka is the  Legend....she
# is the great women
# she also intelligence''')
# Use constants: declare a value as a constant by convention (ALL_CAPS) and
# PI = 3.14
# area = float(input("inter the area :"))
# circle_area = PI * area * area
# print("area of the circle:",circle_area)
# 2. Use enum. Enum for symbolic constants
# from enum import Enum
# class Chocklet(Enum):
#     DEARY_MILK = 1
#     FIVE_STAR = 2
#     KITCAT = 3
# print(Chocklet.DEARY_MILK.value)
# 1. Read an integer and determine if it is positive, negative, or zero.
# num = int(input("enter the integer number: "))
# x = 'positive' if num > 0 else 'zero' if num == 0 else 'negative'
# print("the given number is:", x)
# Read two integers and compare them (equality and greater/less).
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# if num1 > num2:
#     print("the number first is greater than second number")
# elif num1 == num2:
#     print("the number first is equal to second number")
# elif num1 < num2:
#     print("the number second is greater then the first number")
# else:
#     print("please enter the correct number")
# # 3. Read three integers and print the smallest and largest.
# num3 = int(input("enter the third number:"))
# if num1 > num2 and num1 > num3:
#     print("number first is greater number")
#     if num2 < num3:
#         print("number second is the smaller number ")
#     else:
#         print("number third is the smaller number ")
# elif num2 > num1 and num2 > num3:
#     print("number second is greater number")
#     if num1 < num3:
#         print("number first is the smaller number ")
#     else:
#         print("number third is the smaller number ")
# else:
#     print("number third is greater number")
#     if num2 < num1:
#         print("number second is the smaller number ")
#     else:
#         print("number first is the smaller number ")
# 4. Check if a number is odd or even.
# x = 'even' if(num1 % 2 == 0) else 'odd'
# print("the given number is the :",x)
# 5. Determine if a year is a leap year.
# if (num1 % 2 == 0 and num1 % 100 !=0) or (num1 % 400 == 0):
#     print("the year is the leap year:", num1)
# else:
#     print("the year is not the leap year:", num1)
# 6. Input a character and check if it's an alphabet
# char = input("enter the character: ")
# # if  'a' <= char <= 'z':
# #     print("the given char is alphabet: ",char)
# # else:
# #     print("the given char is does not the char:", char)
# Read marks for five subjects and assign a grade based on the percentage.
# i = int(input("enter the student mark:"))
# total = 0
# for i in range(5):
#     marks = int(input("enter the student mark:"))
#     # print(marks)
#     total += marks
# total = total / 5
# print(total)
# if total >= 95:
#     print("the grade is A")
# elif total >= 80:
#     print("the grade is B")
# elif total >= 70:
#     print("the grade is C")
# else:
#     print("the grade is D")
# Compute profit or loss given the cost price and the selling price.

# cost_price = float(input("Entert the cost price:"))
# selling_price = float(input("Enter the selling price:"))
# if selling_price >= cost_price:
#     print("we are in the Profit")
# else:
#     print("We are in the loss")
# Input angles and check if they form a valid triangle.
# trangle = 0
# for i in range(3):
#     angle = int(input("enter the angle: "))
#     if angle > 0:
#         trangle += angle
#     print(trangle)
    # if trangle == 180:
    #     print("angle form the valid triangle:")
    # else:
    #     print("angle not form the valid trangle")
    # else:
    # print("enter the angle value greater then the 0")


# Input angles and check if they form a valid triangle.
# total = 0
# # for i in range(3):
# angle1 = int(input("enter the angle: "))
# angle2 = int(input("enter the angle: "))
# angle3 = int(input("enter the angle: "))
# print(angle1, angle2, angle3)
#
# if angle1 > 0 and angle2 > 0 and angle3 > 0 and total == 180:
#     total = angle1 + angle2 + angle3
#     print("angle is the make triangle:",total)
# else:
#     print("angle must be greater then 0:")

# total = 0
# # for i in range(3):
# for i in range(3):
#     angle = int(input("enter the angle: "))
#     print(angle)
#     if angle > 0:
#          total += angle
#
#     else:
#        print("angle must be greater then 0:")
#        break
#
# if total == 180:
#     print("the angle's form the trangle")
# else:
#     print("angle not form the trangle")
# 4. Input sides, check for triangle validity, and classify (equilateral, isosceles,scalene)
# total = 0
# side1 = int(input("Enter the sides: "))
# side2 = int(input("Enter the sides: "))
# side3 = int(input("Enter the sides: "))
# total = side1 + side2 + side3
# if side1 > 0 and side2 > 0 and side3 > 0 and total == 180:
#     if side1 == side2 == side3:
#         print("the side makes equilateral trangle")
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         print("the side make the  isosceles trangle")
#     else:
#         print("the side make the scalene trangle")
# else:
#     print("enter the greater than zero value of the side")
# 5. Input the week number (1–7) and print the corresponding weekday name.

# day_s = int(input("enter the number: "))
# day_s = ["Sunday", "monday", "Tusday","Wensday","Thursday", "Friday", "Saturday"]
# if 1 <= week <= 7:
#     print("the day is:", day_s[week-1])
#
# else:
#     print("enter the correct day number :")
# Input a month number (1–12), display days in the month (handle leap years forFebruary).
# month = ['jan', 'mar','may','jul','aug','oct', 'dec']
# year = int(input("Enter the year"))
# day_s = int(input("enter the number: "))
# month = [1,3,5,7,8,10,12]
# if day_s in month:
#     print("the 31 day in this month")
# elif day_s == 2:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("the 29 days in this month")
#     else:
#         print("the 28 days in this month")
# elif day_s in [2,4,6,9,11]:
#     print("the 30 days in this month")
#
# else:
#     print("Enter the month number in between the 1 to 12")
# Simple calculator using match-case for operations (+, -, *, /)

# num1 = int(input("enter the number: "))
# num2 = int(input("enter the number: "))
# op = input("enter the operator: ")
# match op:
#     case "+":
#         print("addition", num1 + num2   )
#     case "*":
#         print("multiplication", num1 * num2 )
#     case "-":
#         print("subtraction", num1 - num2 )
#     case "/":
#         print("division", num1 / num2 )
#     case _:
#         print("invalid operator")

# Print weekday based on user number input using match-case.
# num = input("Enter the number: ")
# match num:
#     case '1':
#         print("the day is Monday")
#     case '2':
#         print("the day is Tuesday")
#     case '3':
#         print("the day is Wednesday")
#     case '4':
#         print("the day is Thursday")
#     case '5':
#         print("the day is Friday")
#     case '6':
#         print("the day is Saturday")
#     case '7':
#         print("the day is Sunday")
#     case _:
#         print("the day is unknown")
# 3. Input grade character and print remarks using match-case.
# grede = input("Enter the grede charactor")
# match grede:
#     case "A":
#         print("very goog grede",grede)
#     case "B":
#         print("good grede",grede)
#     case "C":
#         print("bad grede",grede)
#     case _:
#         print("out-of-range input")
# Find the maximum of two numbers using the ternary operator.
# num1 = int(input("Enter the num1"))
# num2 = int(input("Enter the num2"))
# x = num1 if num1 > num2 else num2
# print("Max is:",x)
# Determine even/odd using the ternary operator
# num = int(input("enter the number"))
# x = 'even' if num % 2 == 0 else 'odd'
# print(x)
# Assign "Pass"/"Fail" based on marks using the ternary operator
# marks = float(input("Enter the marks: "))
# x = 'pass'if 35 <= marks <= 100 else 'Fail'
# print(x)
# 4. Classify a number as positive/negative/zero using nested ternary operators.
# num = int(input("enter the number"))
# x = 'Positive' if num> 0 else 'Negative' if num < 0 else 'Zero'
# print(x)

# 1. Check for invalid (non-numeric) integer input using exception handling(try/except).


# try:
#     num = int(input("enter the number: "))
#     if num >= 0:
#         print("this is positive number:",num)
#     else:
#         print("this is negative number:", num)
# except ValueError:
#     print("this is nun-numeric")

# Print error messages for inputs outside expected ranges.
# try:
#    num = int(input("enter the number: "))
#    if 0 <= num <= 10:
#        print("the number is between 0 and 10", num)
#    else:
#        print("the number is between 0 and 10")
# except ValueError:
#     print("input outside expected range")
# # 1. Print numbers from 1 to n.
# n = int(input("Enter the number: "))
# i = 0
# while i <= n:
#     print(i)
# #     i += 1
# sum = 0
# # Sum integers from 1 to n.
# while i <= n:
#     sum += i
#     i += 1
# print(sum)
# for i in range(n+1):
#     sum += i
# print(sum)
# # 3. Print the multiplication table of a number.
# while i <= 10:
#     print(f"the multiplication table of {i} : {i * n}")
#     i += 1
# 4. Reverse a number entered by the user.
# while n > 0:
#     digit = n % 10
#     i = i * 10 + digit
#     n = n // 10
# print(i)
# digit = 0
# while i <= n:

# Reverse a number entered by the user

# n = int(input("enter the number: "))
# i = n
# while i > 0:
#     i = i - 1
#     print(i)
# -------------------------------
#
# n = int(input("enter the number: "))
# i = 0
# while   n > 0:
#     digit = n % 10
#     i = i * 10 + digit
#     n = n // 10
#     # print(digit)
#     print(n)


# Count and display the number of digits in a number
# digit = int(input(" Enter the digit: "))
# count = 0
# while digit > 0:
#     # num = digit % 10
#     # count = count * 10 + num
#     digit //= 10
#     count += 1
# print(count)

# Calculate factorial using a while loop.
# digit = int(input(" Enter the digit: "))
# count = digit
# total = 1
# while count > 0:
#     total = total * count
#     count -= 1
# # print(total)
# num = int(input(" Enter the digit: "))
# # count = digit
# total = 1
# while num > 0:
#     total = total * num
#     num -= 1
# print(total)
# Print numbers from 1 to n
# num = int(input("Enter the number: "))
# i = 0
# # while i <= num:
#     print(i)
#     i += 1
# for i in range(1, num + 1):
#     print(i)
# Sum integers from 1 to n.
# sume = 0
# while i <= num:
#     sume += i
#     print(sume)
#     i += 1
# for i in range(num + 1):
#     sume += i
# print(sume)

# Calculate factorial using a while loop
# n = int(input("Enter the number: "))
# fact = 1
# while n > 0:
#     fact = fact * n
#     n -= 1
# print(fact)

# 5. Count and display the number of digits in a number
# i = 0
# while n > 0:
#     n = n // 10
#     i += 1
# print(i)

# 8. Print the first n terms of the Fibonacci sequence.

# a, b = 0, 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b
# 9. Display all prime numbers from 1 to 100.
# for i in range(2, n+1):
#     is_prime = True
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i,"is prime number")

# 10.Calculate the sum of the series 1 + 1/2 + ... + 1/n
# sum = 0
# i = 1
# for i in range(1, n+1):
#     print(sum)
#     if i != 0:
#       sum += 1 / i
#       print("term",1/i)
#       # sum += i
#       # print(sum)
#     else:
#         print("Cannot do the operation")

# for i in range(1, n+1):
#     print(sum)
#     # if i != 0:
#     sum += 1 / i
#     print("term",1/i)


# 1. Print uppercase ASCII characters and their codes.

# for i in range(65, 91):
#     print(chr(i), '>',i)

# 12.Create star patterns (square, triangle) of user-given height.
height = int(input("Enter the height:"))
for i in range(height,0,-1):
    print('*' * i)
    for j in range(height,0,-1):
        print('*' * j)