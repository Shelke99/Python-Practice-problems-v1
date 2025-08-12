# Input Validation and Error Handling
# 1. Check for invalid (non-numeric) integer input using exception handling(try/except).
num = input("Enter a number: ")
try:
    num = int(num)
    print(num)
except ValueError:
    print("That's not a number")