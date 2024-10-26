import pandas as pd

df = pd.read_csv("GoogleApps.csv")
print(df.info())
temp = df.groupby(by='Type')['Rating'].agg(['min','mean','max']) #мінімальний, середній та максимальний рейтинг
print(temp)

temp = df[df['Type']=='Paid'].groupby(by='Content Rating')['Price'].agg(['min','median','max'])
#мінімальну, медіанну (median) та максимальну ціну ('Price') платних додатків (Type == 'Paid')
print(temp)



