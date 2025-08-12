
# Check if the character is a vowel or a consonant.
char = input("enter a character:")
# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#     print(char,"is vowel")
# else:
#     print(char,"is not charactor")
#
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
if len(char) == 1 and char.isalpha():
    if char in vowels:
        print(f"given charactor is {char} is vowel")
    else:
        print(f"given charactor is {char} is not vowel")
else:
    print("please enter a single character")



