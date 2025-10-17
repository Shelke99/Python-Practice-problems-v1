def IsPalindrome():
    num = input("Enter the num:")
    i = 0
    j = int(len(num)) - 1
    flag = True
    while i < j:
        if num[i] == num[j]:
            i += 1
            j -= 1

        else:
            flag = False
            break
    if flag:
        print("The number is palindrome", num)
    else:
        print("The number is not palindrome",num)
IsPalindrome()