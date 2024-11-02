import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("Ankara Rent Prices/ultimate_rent_price_dataset.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[df['Price'] <= 100000]
df = df[df['Area'] <= 500]

mean_location_price = df.groupby('Location')['Price'].mean()
df['Location_Encoded'] = df['Location'].map(mean_location_price)

encoder = OrdinalEncoder()
df['Floor_Encoded'] = encoder.fit_transform(df[['Floor']])
df = df.drop(columns=['Floor','Location','Rooms'])

df.to_csv("Ankara Rent Prices/modeling_data.csv")
