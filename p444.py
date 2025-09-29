# 5. Input the week number (1–7) and print the corresponding weekday name
print("number should be positive and lessthan 8")
num = int(input("Enter a number: "))
if num > 0 and num <= 7:
    if num == 1:
        print(" is SUNDAY")
    elif num == 2:
        print(" is MONDAY")
    elif num == 3:
        print(" is TUSDAY")
    elif num == 4:
        print(" is WEDNESSDAY")
    elif num == 5:
        print(" is THURSDAY")
    elif num == 6:
        print(" is FRIDAY")
    else:
        print(" is SATURDAY")
else:
    print(" Enter the number in between the 1 and 7")

