# 21.Count vowels and consonants in a string.
str = input("Enter the string:")
vowels = 0
consonants = 0
for chr in str:
    if chr.isalpha():
        if chr.lower() in ['a','e','i','o','u']:
           vowels += 1
        else:
           consonants += 1
print("The vowel count is:", vowels)
print("The consonant count is:", consonants)
