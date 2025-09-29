# . Read an integer and determine if it is positive, negative, or zero.
#
# num = int(input("ënter the number:"))
# if num > 0:
#     print("num is positive")
# elif num < 0:
#     print("num is negative")
# else:
#     print("num is zero")

# 2. Read two integers and compare them (equality and greater/less).
# num2 = int(input("Enter the number second:"))
# if num > num2:
#     print("number first is greater than number second",num, num2)
# elif num < num2:
#     print("number first is less than number second",num, num2)
# elif num == num2:
#     print("num and num2 is equal",num,num2)
# else:
#     print("enter the number")
# 3. Read three integers and print the smallest and largest
# num3 = int(input("Enter the number third:"))
# if num2 < num and num3 < num:
#     print("num is largest")
# elif num < num2 and num3 < num2:
#     print("num2 is largest")
# elif num < num3 and num2 < num3:
#     print("num3 is largest")
# elif num < num2 and num < num3:
#     print("first num is smallest")
# elif num2 < num and num2 < num3:
#     print("second num is smallest")
# elif num3 < num and num3 < num2:
#     print("third num is smallest")
# else:
#     print("enter the number")
# 4. Check if a number is odd or even.
#
# num = int(input("enter the number:"))
# if num % 2 == 0:
#     print("num is even")
# else:
#     print("num is odd")
# 5. Determine if a year is a leap year
# year = int(input("Enter year: "))
# if (year % 4 == 0 and year / 100 ) or year % 400 == 0:
#     print("year is leap")
# else:
#     print("year is not leap")
# 6. Input a character and check if it's an alphabet.
# char = input("Enter a alphabet: ")
# if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') :
#     print("its a alphabet")
# else:
#     print("it is not a alphabet")
# 7. Check if the character is a vowel or a consonant.
# if char == "a" or char == "i" or char == "e" or char == "u" or char == "o":
#     print("Yes")
# else:
#     print("No")
#     print(char)
# 8. Check if a character is uppercase, lowercase, a digit, or a special character.
# if char >= "a" and char <= "z":
#     print("the charactor is the lower case")
# elif char >= "A" and char <= "Z":
#     print("the charactor is the upper case")
# elif char >= "0" and char <= 9:
#     print("the charactor is the digit")
# else:
#     print("the charactor is the special character")

# 3. Read three integers and print the smallest and largest.

# if num >num2 and num >num3:
#     print("num is largset")
#     if num2 > num3:
#         print("num 3 is smaller")
#     else:
#         print("num2 is smaller")
# elif num2 >num and num2 >num3:
#     print("num2 is largset")
#     if num > num3:
#         print("num 3 is smaller")
#     else:
#         print("num is smaller")
# else:
#     print("num3 is largset")
#     if num2 > num:
#         print("num is smaller")
#     else:
#         print("num2 is smaller")

# 1. Read marks for five subjects and assign a grade based on the percentage.
# s1 = float(input("enter the subject1 mark:"))
# s2 = float(input("enter the subject2 mark:"))
# s3 = float(input("enter the subject3 mark:"))
# s4 = float(input("enter the subject4 mark:"))
# s5 = float(input("enter the subject5 mark:"))
# total = s1 + s2 + s3 + s4 + s5
# percentage = total // 5
# if percentage >= 95:
#     print("grade 'A'", percentage)
# elif percentage >= 80:
#     print("grade 'B'", percentage)
# elif percentage >= 70:
#     print("grade 'C'", percentage)
# else:
#     print("grade 'D'", percentage)


# 2. Compute profit or loss given the cost price and the selling price.
# cost_price = float(input("Enter cost price: "))
# selling_price = float(input("Enter selling price: "))
# total_price = cost_price + selling_price
# if cost_price > selling_price:
#     print("we'r in loss")
# elif cost_price == selling_price:
#     print("we'r nither loss or nither profit")
# else:
#     print("we'r in profit")
# 4. Handle out-of-range input with a default message.
# msg = input("Enter a message: ")
# match msg:
#     case "1":
#         print("Hello World!")
#     case "2":
#         print("Goodbye World!")
#     case _:
#         print("Sorry, I don't understand.please enter the correct number")



# 1. Find the maximum of two numbers using the ternary operator
# a = int(input("enter the number1"))
# b = int(input("enter the number2"))
# c =  a if a > b else b
# print(c)

# 2. Determine even/odd using the ternary operator.
# num = int(input("enter the number:"))
# x = "even" if (num % 2 == 0) else "odd"
# print(x)

# # Assign "Pass"/"Fail" based on marks using the ternary operator.
# mark = float(input("Enter marks: "))
# x = "pass"if mark >= 35 else "fail"
# print(x)
# Classify a number as positive/negative/zero using nested ternary operators.
# num = int(input("Enter a number: "))
# x = "positive" if num > 0 else "zero" if num ==0 else "negative"
# print(x)