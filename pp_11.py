# Read three integers and print the smallest and largest.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
maxn = 0
minn = 0
if num1 > num2 and num1 > num3:
    maxn = num1
    if num2 > num3:
        minn  = num3
        print(minn)
    print(maxn)
elif num2 > num1 and num2 > num3:
    maxn = num2
    if num3 > num1:
        minn = num1
        print(minn)
    print(maxn)

elif num3 > num1 and num3 > num2:
    maxn = num3
    if num1 > num2:
        minn = num2
        print(minn)
    print(maxn)


# ------------------------------------------------
