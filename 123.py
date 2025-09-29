# 3. Input grade character and print remarks using match-case.
def grade(grd):
    match grd:
        case "A+":
            return "very good student"
        case "A":
            return "good student"
        case "B":
            return "Average student"
        case "C":
            return "pore in study"
        case "D":
            return "need to more studay"

char = input("enter the character:")
print(grade(char))