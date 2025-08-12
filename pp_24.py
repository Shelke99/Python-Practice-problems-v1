# 4. Handle out-of-range input with a default message.
num = int(input("Enter a number in between 1 to 3: "))
match num:
    case 1:
        print("you enter the number 1")
    case 2:
        print("you enter the number 2")
    case 3:
        print("you enter the number 3")
    case _:
        print("you entering the wrong number...you enter the correct number inbetween 1 and 3")