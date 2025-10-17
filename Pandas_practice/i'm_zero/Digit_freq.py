# Count digit frequency in an integer using loops and list/dictionary
digit = int(input("Enter the digit:"))
# lst = [0] * 10
# for num in str(digit):
#     lst[int(num)] += 1
# print(lst)

# # by using list
# def Digifreq(num):
#     lst = [0] * 10
#     for i in str(num):
#        lst[int(i)] += 1
#     print(lst)
# Digifreq(54321123)

# by using dict
dic = {}
for i in str(digit):
    dic[int(i)] = dic.get(int(i), 0) +1
print(dic)