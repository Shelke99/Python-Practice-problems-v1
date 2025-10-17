def Average_positive_until_zero():
    total = 0.0
    count = 0
    while True:
        try:
            num = float(input("enter the number(0 enter stop) : "))
        except ValueError:
            print("enter the valid number :")
            continue

        if num == 0:
            break
        if num > 0:
            total += num
            count += 1
        else:
            pass

    if count == 0:
        print("No positive number entered: average undefined")
    else:
        average = total / count
        print("the average of positive number is:", average)
Average_positive_until_zero()