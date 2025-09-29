# 24. Keep reading input until a sentinel value (e.g., -99) is entered.
while True:
    num = int(input("enter the number:"))
    if num == -1:
        break
    else:
        print("the number is:", num)