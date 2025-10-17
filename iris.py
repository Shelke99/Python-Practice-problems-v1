import  pandas as pd
#Read data from csv file into a data frame
df = pd.read_csv(r'C:\Users\SUKUN\Downloads\IRIS (1).csv') #encoding= 'utf-8/latin1
print(df.head())

df.to_json(r'C:\Users\SUKUN\Downloads\IRIS (1).json', index = False)

