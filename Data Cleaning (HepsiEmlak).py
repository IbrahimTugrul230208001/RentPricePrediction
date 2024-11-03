import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
df = pd.read_csv("hepsiemlak_rent.csv")
df_1 = pd.read_csv("datasets/rent_listing_prices_encoded.csv")
df = df.drop_duplicates()

df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).str.replace('.', '', regex=False).astype(int)
df['Rooms'] = df['Rooms'].str.extract(r'(\d+)\s*\+\s*(\d+)').apply(lambda x: '+'.join(x.dropna()), axis=1)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['Area'] = df['Area'].str.replace(' m²','',regex=True).astype(int)
df['Location'] = df['Location'].str.replace('Ankara / ','')
df['Location'] = df['Location'].str.replace('Mah.','Mh.')
df['Location'] = df['Location'].str.replace('/','-')
df[['Num_Rooms', 'Num_Halls']] = df['Rooms'].str.split('+', expand=True)
df[['Num_Rooms', 'Num_Halls']] = df[['Num_Rooms', 'Num_Halls']].astype(float)


df_1 = df_1.loc[:, ~df_1.columns.str.contains('^Unnamed')]
df_1 = df_1.drop(columns=["Floor_Encoded","Location_Encoded"],axis=1)

df_new = pd.concat([df,df_1])
df['District'] = df['Location'].str.split('-').str[0].str.strip()

#df_new.to_csv("ultimate_rent_price_dataset.csv")