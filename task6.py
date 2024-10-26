import pandas as pd
df= pd.read_csv("GoogleApps.csv")
print(df.info())

#temp = df.groupby(by='')['Rating'].mean()

print(df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean())

