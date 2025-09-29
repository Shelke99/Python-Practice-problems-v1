# 5. Count and display the number of digits in a number.
num = input("enter a number: ")
digit = num
count = 0
# print(count[0])
# print(digit[0])

for i in digit:
    if digit[i] > "0":
        count += 1
        print(count)
    else:
        break