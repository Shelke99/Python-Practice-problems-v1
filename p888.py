# 6. Input a month number (1–12), display days in the month (handle leap years for
# February).
num = input("enter the number in between the 1 and 12 :")
data = {"1" : "30", "2" : "28", "3" : "30", "4" : "30", "5" : "30", "6" : "30", "7" : "30", "8" : "30", "9" : "30", "10" : "30", "11" : "30", "12" : "30" }
if num in data.keys():
    print(data[num])
else:
    print("Hamare yaha sirf! 12 month hi hote hai")
