import pandas as pd

df = pd.read_csv("GoogleApps.csv")

#print(df.info())
df['Reviews'] = pd.to_numeric(df['Reviews'])
#print(df['Reviews'])
temp = df.groupby(by='Category')['Reviews'].max()
print(temp)
