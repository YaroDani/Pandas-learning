import pandas as pd
df= pd.read_csv("GoogleApps.csv")
#print(df.info())

temp = df[(df['Category'] == 'GAME') & (df['Rating']> 4.9)]['Type'].value_counts()
print(temp['Free']/temp['Paid'])

#tempp=(df[(df['Price'] > 0) & (df['Rating'] > 4.9)]['Rating'].value_counts())
#tempf=(df[(df['Price'] == 0) & (df['Rating'] > 4.9)]['Rating'].value_counts())

#print(tempp/tempf)