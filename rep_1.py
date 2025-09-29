# a = "Hello World"
# print(a)
# b = 12
# print(b)
# c = int(input("enter the integer value:"))
# d = int(input("enter the another integer value:"))
# print(d)
# print(c)

#addition
# print(c + d)
# print(c - d)
# print( c * d)
# print(c // d)
# print(c % d)

# nm = c + d
# print(nm)
# nm2 = c - d
# print(nm2)
#
# nm3 = c * d

# print(nm3)

# temp = c
# c = d
# d = temp
# c, d = d, c
# b = 12
# print(b, type(b))
# print(b, id(b))
# c = True
# print(c, type(c))
# print(c, id(c))
# print(a, type(a))
# print(a, id(a))
# d = 2.3
#
# print(d, id(d))
# print(d,type(d))
# a = 'priya'
# print(a)
# p = 'a'
# print(p)

# st = input("Enter the String:")
# # print(f"'\n'+str(st)")
# print("\n"+str(st))
# print(f"\n{st}")
# 2. Use enum. Enum for symbolic constants.
from enum import Enum
class colors(Enum):
    RED = 1
    GREEN = 2
    blue = 3
print(colors.RED.value)
print(colors.RED)
print(colors.blue.name)




