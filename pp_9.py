# Section 2: Conditional Statements and Input Validation
# 2.1 Basic If, Elif, Else
# Read an integer and determine if it is positive, negative, or zero.
num = int(input("enter the integer number:"))
if num > 0:
    print(num,"is positive number")
elif num < 0:
    print(num, "num is negative number")
else:
    print(num, "is zero number")