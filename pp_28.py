# 2. Print error messages for inputs outside expected ranges.

try:
    num = int(input("enter the number between the given 10 AND 100 range: "))
    if 10 <= num <= 100:
        print(f"this is valid number is : {num}")
    else:
        print("the given input is out of the range:betn 10 nad 100")
except ValueError:
    pass
    #print("Error: Please enter a valid integer.")
