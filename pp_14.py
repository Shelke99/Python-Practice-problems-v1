#Input a character and check if it's an alphabet.
char = input("Enter a character: ")
# if char.isalpha():
#     print("The character is alphabet", char)
# else:
#     print("The character is not alphabet", char)

# -------------------------------------------------------------------------
# Check if a character is uppercase, lowercase, a digit, or a special character.
if char.isalpha():
    if char.isupper():
        print(f"given char is uppercase {char}")
    else:
        print("given char is lowercase")
else:
    print("enter the alphanumeric character")