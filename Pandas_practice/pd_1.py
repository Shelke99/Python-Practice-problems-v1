import pandas as pd
data = {
    "name" : ['ram',"Sham","Ghanshyam"],
     "age" : [10,20,30],
     "City" : ["Nagpur","Satara",'DELHI']

}
df = pd.DataFrame(data)
print(df)
# df.to_excel('data.xlsx',index=False)
df.to_json('data.json')