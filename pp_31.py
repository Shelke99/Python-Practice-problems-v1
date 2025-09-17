
# 2. Sum integers from 1 to n
result = 0
n = int(input("enter the number "))
num = 1
while num <= n:
    result += num
    num += 1
print("the result is", result)