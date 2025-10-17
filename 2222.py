# Match-Case (Python 3.10+) & Elif Chains
# 1. Simple calculator using match-case for operations (+, -, *, /).
def operator(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Divisible by zero"
        case '_':
            return "invalid operator"

num1 = float(input("enter the number:"))
num2 = float(input("enter the number:"))
op = input("enter the operator:")
result = operator(num1, num2, op)
print(result, "result is")