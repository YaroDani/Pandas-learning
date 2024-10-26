import pandas as pd

df = pd.read_csv("GoogleApps.csv")

print(df.info())

print(df['Type'].unique())
#df['Reviews'] = df['Reviews'].str.replace('M', '')
#df['Reviews'] = pd.to_numeric(df['Reviews'])

temp = df.groupby(by='Type')['Reviews'].max()
print(temp)
