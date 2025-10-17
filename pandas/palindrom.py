num = input("enter the number:")
i =0
j = len(num) - 1
while i < j:
    is_flag = 0
    if num[i] == num[j]:
        i += 1
        j -= 1
        # print("number is palindrome:", num)
    else:
        # print("the number is not palindrome",num)
        is_flag = 1
        break

if is_flag == 0:
    print("the number is palindrome")
else:
    print("the number is not palindrome")

