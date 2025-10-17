import pandas as pd
data = {
    "Student_id" : [1,2,3,4,5],
    "name" : ["Rahul", "Priya", "Amit", "Sneha", "Neha"],
    "age" : [17, 16, 17, 16, 17],
    "Gender" : ["M", "F", "M", "F", "F"],
    "math" : [78, 88, 67, 92, 85],
    "Science": [67, 79, None, 90, 95],
    "English" : [80, None, 70, 88, 89],
    "Attendance" : [85, 90, 60, None, 95],
    "City" : ["Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore"]
}
# df = pd.DataFrame(data)
# print(df)

# we have to check data info and summary
# df.info()

# print(df.isnull().sum())
df["Science"].fillna(df["Science"].mean(), inplace = True)
df["English"].fillna(df["English"].median(), inplace=True)
df["Attendance"].fillna(75, inplace=True)
df["Total"] = df["Science"] + df["Science"] + df["English"]
print(df)
df["Average"] = df["Total"] / 3