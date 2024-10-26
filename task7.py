import pandas as pd
df= pd.read_csv("GoogleApps.csv")
print(df.info())

temp = df['Content Rating'].value_counts()

print(temp['Teen']/temp['Everyone 10+'])

