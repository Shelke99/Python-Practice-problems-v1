def StrPalindrome():
    string = input("Enter the string:")
    i = 0
    j = len(string)-1
    flag = True
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
            continue
        else:
            flag = False
            break
    if flag:
        print("The string is palindrome", string)
    else:
        print("The string is not palindrome", string)
StrPalindrome()