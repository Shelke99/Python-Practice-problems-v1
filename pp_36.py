# 19.Calculate the average of positive numbers entered (stop on zero)
sum = 0
count = 0
while True:
    num = int(input("enter the number:"))
    if num < 0:
        print("this is the negative number:",num)
        break
    else:
        sum += num
        count += 1

avg = sum / count
print("the average is",avg)
