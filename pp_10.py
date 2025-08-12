# Read two integers and compare them (equality and greater/less).

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
    print(num1, "num1 is greater and",num2, "num2 is less")

# elif num1 < num2:
#     print(num2, "num2 is greater and ",num1,"num1 is less than ")

elif num1 == num2:
    print(num1, "num1 is equal to",num2,"num2 is equal to")
