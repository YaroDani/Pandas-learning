import pandas as pd
i=0
df = pd.read_csv("GoogleApps.csv")
print(df.info())
#print(df[df['Category'] == 'BUSINESS'])
#print(df.tail(1))
print(df['Installs'].median())
