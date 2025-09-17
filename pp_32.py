# 3. Print the multiplication table of a number.
number = int(input("please enter the number "))
for j in range(1,number):
    i = 1
    print(f"table of {j}")
    while i <= 10:
        print(f"i * j : {i * j}")
        i += 1
