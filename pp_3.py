#read an integer from the user and print it.
for _ in range(2):
    a = int(input("enter the integer number:"))
    print(a)

#---------------------
#Add, subtract,and Multiply two integers(without third variable)
b = 30
c = 40
print("Addition of two number is:", b + c)
print("Subtraction of two number is:", b - c)
print("Multiplication of two number is:", b * c)


#----------------------------------
#Add, subtract,and Multiply two integers(using third variable)
b = 30
c = 40
result = b + c
result1 =  b - c
result2 = b - c
print("Addition of two number is:", result)
print("Subtraction of two number is:",result1)
print("Multiplication of two number is:",result2)

#---------------------------------
#Swap to numbers using third variable
print("before swapping the values ...value of b", b, "and the value of c :", c)

temp = b
b = c
c = temp
print("after the swapping the values ...value of b", b, "and the value of c :", c)
#------------------------------
#Swap to numbers without using third variable(pythonic way)1
# python allow  tuple unpacking, so you can swap values in oneline without a temperary vatiable
i = 20
j = 30
print("before swapping the values ...value of i", i, "and the value of j :", j)
i, j = j, i

print("after the swapping the values ...value of i", i, "and the value of j :", j)

#--------------------------------------------------------------------------------------------
#print the type and ID(type(), id()) of basic variables(int, float,str, bool).
z = int(input("enter the integer value of z:"))
print("type of z:", type(z), "and ID of z is:", id(z))

#float
x = float(input("enter the integer value of x:"))
print("type of x:", type(x), "and ID of x is:", id(x))

#bool
y = bool(input("enter the integer value of y:"))
print("type of y:", type(y), "and ID of y is:", id(y))

r = input("enter the integer value of r:")
print("type of r:", type(r), "and ID of z is:", id(r))
#--------------------------------------------------------------------------------------

#Assign a character to a variable and print it.
char = 'a'
print(char)