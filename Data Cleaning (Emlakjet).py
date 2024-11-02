'''
df['Price'] = df['Price'].str.replace(' TL','',regex=False)
df['Price'] = df['Price'].str.replace('.','',regex=False)
df['Price'] = df['Price'].astype('int')
df['Rooms'] = df['Rooms'].str.replace('weekend', '', regex=False).str.strip()
df['Area'] = df['Area'].str.replace('texture', '', regex=False).str.strip()
df['Floor'] = df['Floor'].str.replace('layers', '', regex=False).str.strip()
df['Floor'] = df['Floor'].fillna("Belirsiz")
df['Location'] = df['Location'].str.replace('Ankara - ', '', regex=False)
df = df.drop_duplicates()
df['Area'] = df['Area'].str.replace(' m²','',regex=False).astype(int)
df = df[~df['Rooms'].str.contains('Stüdyo', na=False)]
df = df[~df['Rooms'].str.contains('9\+ Oda', na=False)]
df.loc[df['Rooms']=="1 Oda",'Rooms'] = "1+0"
df[['Num_Rooms', 'Num_Halls']] = df['Rooms'].str.split('+', expand=True)
df[['Num_Rooms', 'Num_Halls']] = df[['Num_Rooms', 'Num_Halls']].astype(float)


df = pd.read_csv("datasets/rent_listing_prices_encoded.csv")

df['District'] = df['Location'].str.split(' - ').str[0]
df = df.drop(columns=['Location','Rooms','Location_Encoded','Floor_Encoded'],axis=1)

# Initialize OneHotEncoder with the updated parameter
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Apply one-hot encoding to 'Floor' and 'District'
encoded_columns = encoder.fit_transform(df[['Floor', 'District']])

# Retrieve the new column names from the encoder
encoded_column_names = encoder.get_feature_names_out(['Floor', 'District'])

# Convert the encoded columns to a DataFrame
encoded_df = pd.DataFrame(encoded_columns, columns=encoded_column_names)

# Concatenate the original df with the encoded columns, dropping 'Floor' and 'District'
df_final = pd.concat([df.drop(['Floor', 'District'], axis=1), encoded_df], axis=1)

# Print the final DataFrame
df_final.to_csv("Ankara Rent Prices/rent_onehot_encoded.csv")
'''
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,OrdinalEncoder

df = pd.read_csv("datasets/rent_price_listings.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[~df['Rooms'].str.contains('Stüdyo', na=False)]
df = df[~df['Rooms'].str.contains('9\+ Oda', na=False)]
df.loc[df['Rooms']=="1 Oda",'Rooms'] = "1+0"
df[['Num_Rooms', 'Num_Halls']] = df['Rooms'].str.split('+', expand=True)
df[['Num_Rooms', 'Num_Halls']] = df[['Num_Rooms', 'Num_Halls']].astype(float)

df = df[df['Price'] <= 100000]
df = df[df['Area'] <= 700]

encoder = OrdinalEncoder()
df['Floor_Encoded'] = encoder.fit_transform(df[['Floor']])
mean_location_price = df.groupby('Location')['Price'].mean()
df['Location_encoded'] = df['Location'].map(mean_location_price)
df = df.drop(columns=['Location','Floor','Rooms'])
print(df)
df.to_csv("Ankara Rent Prices/rent_prices_encoded.csv")