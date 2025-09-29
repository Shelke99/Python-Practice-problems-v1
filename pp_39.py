# Demonstrate an infinite loop (while True:).
num = int(input("How many numbers do you have?"))
while True:
    if num < 0:
        break
    else:
        print("The number is:", num)


