# 2.2 Nested Conditions and Logical Operators
# Read marks for five subjects and assign a grade based on the percentage.

marks = []
for i  in range(1,6):
    mark = float(input(f"enter the mark of subject {i}:"))
    marks.append(mark)
total = sum(marks)
percentage = (total / 500) * 100
print(percentage)
if percentage >= 95:
    print(f"the total mark is {total} and percentage is {percentage}% and gread is A")
elif 95 < percentage and percentage >= 80:
    print(f"the total mark is {total} and percentage is {percentage}% and gread is B")
elif 80 < percentage and percentage >= 70:
    print(f"the total mark is {total} and percentage is {percentage}% and gread is C")
else:
    print(f"the total mark is {total} and percentage is {percentage}% and gread is D")