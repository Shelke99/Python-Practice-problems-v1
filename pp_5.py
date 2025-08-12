#Find the roots of a quadratic equation given coefficients a, b, and c.
import math
a = int(input("enter the value of a:"))
b = int(input("enter the  value of b:"))
c = int(input("enter the value of c:"))

under_root = (b * b) - (4*(a * c))
print(under_root)
root = math.sqrt(under_root)
print(root)
root1 = (-b - root) / (2 * a)
print(root1)
root2 = (-b + root) / (2 * a)
print(root2)