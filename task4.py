import pandas as pd

df = pd.read_csv("GoogleApps.csv")

#print(df['Size'].unique())
'''df['Size'] = df['Size'].str.replace('Varies with device', '')
def converter_size(size):
    if isinstance(size, str):
        if "M" in size:
            return float(size.replace('M', '')) *1024
        elif 'k' in size:
            return float(size.replace('k', ''))
    return None

df['Size'] = df['Size'].apply(converter_size)
temp = df.groupby(by='Content Rating')['Size'].min()
print(temp)'''
print(df.info())
print(df.groupby(by = 'Content Rating')['Size'].min())
