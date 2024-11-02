import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("Ankara Rent Prices/ultimate_rent_price_dataset.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

"""
sns.scatterplot(x="Area",y="Price",hue="Rooms",data=df)
plt.show()
# 1. Price Distribution
plt.figure()
sns.histplot(df['Price'], bins=30, kde=True)
plt.title('Price Distribution')
plt.savefig('price_distribution.png')
plt.show()

# 2. Area Distribution
plt.figure()
sns.histplot(df['Area'], bins=30, kde=True)
plt.title('Area Distribution')
plt.savefig('area_distribution.png')
plt.show()

# 3. Box Plot for Price by Room Count
plt.figure()
sns.boxplot(x='Rooms', y='Price', data=df)
plt.title('Price by Room Count')
plt.savefig('boxplot_price_by_rooms.png')
plt.show()



# 5. Correlation Heatmap
plt.figure()
sns.heatmap(df[['Price', 'Area', 'Num_Rooms', 'Num_Halls']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# 6. Pair Plot
sns.pairplot(df[['Price', 'Area', 'Num_Rooms', 'Num_Halls']])
plt.savefig('pairplot.png')
plt.show()

# 7. Average Price by Number of Rooms (Bar Plot)
plt.figure()
sns.barplot(x='Rooms', y='Price', data=df, estimator=np.mean)
plt.title('Average Price by Number of Rooms')
plt.savefig('average_price_by_rooms.png')
plt.show()

# 8. Average Price by Location (Bar Plot)
plt.figure(figsize=(10, 6))
sns.barplot(x='Location', y='Price', data=df, estimator=np.mean)
plt.xticks(rotation=90)
plt.title('Average Price by Location')
plt.savefig('average_price_by_location.png')
plt.show()

# 9. Violin Plot of Price by Floor Level
plt.figure()
sns.violinplot(x='Floor', y='Price', data=df)
plt.title('Price Distribution by Floor Level')
plt.savefig('violinplot_price_by_floor.png')
plt.show()

# 10. FacetGrid by Rooms and Halls
g = sns.FacetGrid(df, col="Rooms", hue="Num_Halls", col_wrap=4)
g.map(sns.scatterplot, "Area", "Price", alpha=.7)
g.add_legend()
g.savefig('facetgrid_rooms_halls.png')  # FacetGrid does not have a direct save method. Use plt.savefig() after show.
plt.show()

# 11. Room Count Distribution (Count Plot)
plt.figure()
sns.countplot(x='Rooms', data=df)
plt.title('Room Count Distribution')
plt.savefig('room_count_distribution.png')
plt.show()

# 12. Joint Plot of Price and Area
sns.jointplot(x="Area", y="Price", data=df, kind="hex")
plt.savefig('jointplot_area_price.png')
plt.show()

# 13. Swarm Plot of Price by Floor
plt.figure()
sns.swarmplot(x='Floor', y='Price', data=df)
plt.title('Price by Floor')
plt.savefig('swarmplot_price_by_floor.png')
plt.show()
"""

# 4. Box Plot for Price by Floor Level
plt.figure(figsize=(12, 6))  # Increase figure size for better fit
sns.boxplot(x='Floor', y='Price', data=df)
plt.title('Price by Floor Level')

# Rotate x-axis labels for readability and reduce font size
plt.xticks(rotation=45, ha='right', fontsize=8)

# Optional: Adjust spacing to make sure labels fit within the figure area
plt.tight_layout()

# plt.savefig('boxplot_price_by_floor.png')
plt.show()