# 2. Print weekday based on user number input using match-case
def week(num):
    match  num:
        case 1:
            return "today is Monday"
        case 2:
            return "today is Tuesday"
        case 3:
            return "today is Wednesday"
        case 4:
            return "today is Thursday"
        case 5:
            return "today is Friday"
        case 6:
            return "today is Saturday"
        case 7:
            return "today is Sunday"
        case _:
            return "error: week have only 7 days"
number = int(input("Enter the number: "))
print(week(number))

