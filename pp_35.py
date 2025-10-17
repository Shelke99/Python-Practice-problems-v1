# 20. Check if a number is a palindrome.
#1212
num = input("enter the number:")
i =0
j = len(num) - 1
is_flag = True
while i < j:
    if num[i] == num[j]:
        i += 1
        j -= 1

    else:
        is_flag = False
        break

if is_flag:
    print("number is palindrome:", num)
else:
    print("the number is not palindrome", num)


