# Count vowels and consonants in a string.
def Vowels_Count():
    try:
        s = input("Enter a String:")
        vowel_count = 0
        consonants_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for chr in s.lower():
            if chr.isalpha():
                if chr in vowels:
                    vowel_count += 1
                else:
                    consonants_count += 1
        print("Number of vowels:", vowel_count, "Number of consonants:", consonants_count)
    except Exception as e:
        print(e)

Vowels_Count()
