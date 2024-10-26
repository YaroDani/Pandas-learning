import pandas as pd

df = pd.read_csv("GoogleApps.csv")
print(df.info())
'''
print(df['Installs'].mean())

print(df['Installs'].median())

print(df['Price'].max())
'''


'''
temp = df.groupby(by='Type')['Reviews'].max()
print(temp)



df['Reviews'] = df['Reviews'].str.replace('M', '')
df['Reviews'] = pd.to_numeric(df['Reviews'])

temp = df.groupby(by='Content Rating')['Reviews'].mean()
print(temp)



df['Size'] = df['Size'].str.replace('Varies with device', '')
def converter_size(size):
    if isinstance(size, str):
        if "M" in size:
            return float(size.replace('M', '')) *1024
        elif 'k' in size:
            return float(size.replace('k', ''))
    return None
df['Size'] = df['Size'].apply(converter_size)
temp = df.groupby(by='Content Rating')['Size'].min()
print(temp)
'''

#print(df['Category'].value_counts())

'''
temp=df.groupby(by='Type')['Rating'].mean()
print(temp)
'''

'''
tempmax=df.groupby(by='Category')['Size'].max()
tempmin=df.groupby(by='Category')['Size'].min()
print(tempmax['COMICS'])
print(tempmin['COMICS'])
'''
'''
temp=df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])
'''