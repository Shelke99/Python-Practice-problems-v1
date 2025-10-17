import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_excel(r"C:\Users\priyanka.shelke\PycharmProjects\Python-Practice problems-v1\Pandas_practice\claims.csv")
print(df.head())
summary = (df.groupby('hospital_name')['amount'].agg(
    total_claims = 'count',
    total_amount= 'sum',
    avg_amt = 'mean'

).reset_index())

# print(summary)
mean_amt = df['amount'].mean()
std_amt = df['amount'].std()
outliers = df[df['amount'] > mean_amt + 3*std_amt]
# print("Outlier claims:\n", outliers)

# 3️⃣ Plot hospital-wise average claims
summary.plot(kind='bar', x='hospital_name', y='avg_amt', legend=False)
plt.title('Average Claim Amount by Hospital')
plt.ylabel('Amount')
plt.show()




