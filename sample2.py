# print("HELLO WORLD")
# a = 20
# print(a)
# a = int(input("enter the number:"))

# print(a)
# b = int(input("enter the number2:"))
# print(b,"\n")
# print("addition",a + b)
# print("substraction",a - b)
# print("multiplaction",a * b)
# print("division", a/b)
# c = a + b
# print(c)
# d = a - b
# print(d)
# e = a * b
# print(e)
# Swap two numbers using a third variable.
# temp = a
# a = b
# b = temp
# print(a)
# print(b)
# Swap two numbers without using a third variable (Pythonic way).
# a, b = b, a
# print(a)
# print(b)
# 9. Print the type and ID (type(), id()) of basic variables (int, float, str, bool).
# print("variable:",type(a),id(a))
# b = 2.4
# print("variable:",type(b), id(b))
# c = "hello"
# print("variable:", type(c), id(c))
# d = True
# print("Variable",type(d), id(d))
# 10.Assign a character to a variable and print it.
# a = 'S'
# print(a)
# 11. Read a single character and print it.
# char = input("enter the char:")
# if char == "a" or char == "z" or char == "A" or char == "Z":
#     print(char)
# else:
#     print("please enter the only single char")
# 12.Read a string from the user and print it (demonstrate reading with and without
# # spaces).
# char = input("enter the string:")
# print(char)
# char2 = input("enter the string:").split()
# print(char2)
# 1. Evaluate and display the result of arithmetic expressions (test integer division
# vs float division).
# a = int(input("enter the no1"))
# x = int(input("enter the no2"))
# b = float(input("enter the no float1"))
# z = float(input("enter the float2"))
# c = a / b
# f = x / z
# print(c)
# print(f)
# Find the roots of a quadratic equation given coefficients a, b, and c.
# # import math
# a = int(input("enter the value of a"))
# b = float(input("enter the value of b"))
# c = input("enter the value of c")
# # root = (b * b) - 4 *(a * c)
# # print(root)
#
# root2 = math.sqrt(root)
# print(root2)
# real_root = (-b + root2) / (2 * a)
# print(real_root)
# r_root = (-b - root2) / (2 * a)
# print(r_root)
# 3. Read multiple types of data (int, float, str) and print them with formatted
# # output.
# print(f"{a}")
# print(f"{b}")
# print(f"{type(c)}")
# # 4. Demonstrate explicit and implicit type conversions (casting).
# # explicit conversion
# # c = int(b)
# # print(f"{c}")
# # d = float(a)
# # print(f"{d}")
# f = int(c)
# print(f"{type(f)}")
# # Input a character and check if it's an alphabet
# chr = input("enter the value of chr")
# if 'a' <= chr <= 'z' or 'A' <= chr <= 'Z':
#     print(chr)
# else:
#     print("this is not a character")
# 7. Check if the character is a vowel or a consonant.
# if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
#     print("char is th vowel")
# else:
#     print("the chr is the consonent                    ")
# 8. Check if a character is uppercase, lowercase, a digit, or a special character.
# if 'A' <= chr <= 'Z':
#     print("the char is the uppercase")
# elif chr >= 'a' and chr <= 'z':
#     print("the char is the lowercase")
# elif '0' <= chr <= '9':
#     print("the char is the digit")
# else:
#     print("the char is the special character")
# 1. Read marks for five subjects and assign a grade based on the percentage.
# 3. Input angles and check if they form a valid triangle.
# total = 0
# for i in range(3):
#     angle = int(input("enter the value of angle"))
#     if angle > 0:
#         total += angle
#     else:
#         print("value of angle should be greater than 0")
#         break
# if total == 180:
#     print("the given angle make's trangle")
# else:
#     print("the given angle not make's trangle")
# Input sides, check for triangle validity, and classify (equilateral, isosceles,scalene).
# total = 0
# side = int(input("enter the value of side's:"))
# if side > 0:
#     total += side
# else:
#     print("enter the greater than zero side")

# Sum integers from 1 to n.

# n = int(input("enter the number: "))
# i = n

# sample= 0
# while i <= n:
#     sample += i
#     i += 1
# print(sample)


# ans = 0
# for i in range(n):
#     ans += i
#
# print(ans)
# . Print the multiplication table of a number.
# while i <= 10:
#     print(i * n)
#     i += 1
# Reverse a number entered by the user.

# while i > 0:
#     i =  i - 1
#     print(i)

# . Count and display the number of digits in a number
# n = int(input("enter the number: "))
# i = 0
# while i <= n:
#     count = 0
#     # print(i)
#     # i = i + 1
#     if i in count:
#         count = 0
#     else:
#         count += 1
#     print(count)
# count = 0
# ans = 0
# while n > 0:
#     t = n % 10
#     ans =( ans * 10) + t
#     n = n /10
#     print(ans)

# # for i in range(10):
# n = int(input("ënter a digit: "))
# digit = n % 100


# print(digit)

# 4. Reverse a number entered by the user.


# 2. Sum integers from 1 to n.
# n = int(input("enter the num: " ))
# sum = 0
# i = n
# while i <= n:
# for i in range(n + 1):
#     sum += i
# print(sum)

# Print the multiplication table of a number.
# while i <= 10:
#     sum = i * n
#     print(sum)
#     i += 1
# for i in range(1,11):
#     sum = i * n
#     print(sum)
# Reverse a number entered by the user.
# while n > 0:
#     p = n % 10
#     sum = sum * 10 + p
#     n = n // 10
# print("reverse no:", sum)
# while i > 0:
#     i -= 1
#     print(i)
# for i in range(n,1):
#     print(i)
# Count and display the number of digits in a number.
# n = int(input("enter the num: "))
# i = n
# while n > 0:
#     t = n % 10
#     i = i * 10 + t
#     n = n // 10
# print(i)
# while n > 0:
#     n = n // 10
#     i += 1
# print(i)
# 3. Print the multiplication table of a number
# while i <= 10:
#     print(f"the maultiplaction table {n} * {i} is : {i * n}")
#     i += 1
# 2. Sum integers from 1 to n.
# total = 0
# while i <= n:
#     total += i
#     i += 1
# print(total)
# Print numbers from 1 to n.

# while i <= n:
#     i += 1
#     print(i)
# Calculate factorial using a while loop.
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print(fact)
# 7. Print all even numbers between 1 and 100.
# num = int(input("enter a number:"))
# for i in range(1, num + 1):
#     print(i)
# # 8. Print the first n terms of the Fibonacci sequence.
# i = 0
# j = 1
# for i in range(i+j, num+1):
#     i, j = j, i
#     print(i)
# Print all even numbers between 1 and 100
# for i in range(num + 1):
#     print(i)
# . Print the first n terms of the Fibonacci sequence.
# a= 0
# b = 1
# for i in range(num + 1):
#     a, b = b, a + b
#     print(a)
# Calculate the sum of the series 1 + 1/2 + ... + 1/n.
# 15.Print only non-negative values from user input, stop on a negative.
# while True:
#     try:
#        num = int(input("enter the num:"))
#        if num < 0:
#           print("enter the num is negative",num)
#           break
#        else:
#            print(f"this is non_negative value {num}")
#     except ValueError:
#         print("enter the num is invalid")
# while True:
#     num = int(input("ënter the number:"))
#     if num < 0:
#         print(f"negative num{num}")
#         break
#     else:
#         print(f"positive num: {num}")

# 16.Find the smallest divisor of a number greater than 1 using break.
# i = 2
# num = int(input("enter a number:"))
# while True:
#     if num % i == 0:
#         print("smallest divisor of",num, "is", i)
#         break
#     i = i + 1

# # 17. Print multiplication tables for 1 to 10.

# # num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"multiplication table of {i}")
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")

# 12.Create star patterns (square, triangle) of user-given height.
n = int(input("Enter a height: "))
# for i in range(1,num):
#     # print("*")
#     for j in range(1,i+1):
#
#         print("*", end='')
#     print('\n')
# k = num
# for i in range(1, num):
#     for j in range(1, num+1):
#         print("*", end='')
#     print('\n')
#     num -= 1



# 18.Print formatted patterns: pyramid, diamond, Pascal's triangle.
for i in range(n):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\n")