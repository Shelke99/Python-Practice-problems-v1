sum = 0
count = 0
while True:
    num = int(input("Enter the number: "))
    if num == 0:
        break
    if num > 0 :
        sum += num
        count += 1
    else:
        print("the you given number is the negative number:")

if count == 0:
    print("no positive number entered:")
else:
    avg = sum / count
    print(avg)

