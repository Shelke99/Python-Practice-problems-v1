import pandas as pd
import pp_35 as np
data = {
    "name" : ['Ram','Sham', 'Ghanshyam'],
    "Age" : [22,23,24],
    "City" : ['Nagpur','Satara','Delhi']
}
df = pd.DataFrame(data)
print(df)
df = pd.read_json('C:\Users\SUKUN\Downloads\IRIS (1).csv' )