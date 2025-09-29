# 22. Count digit frequency in an integer using loops and list/dictionary.
num = input("enter the digit:")
n = str(num)
count = {}

for i in n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
# print(count)
for i,k in count.items():
    print(i,":",k)
