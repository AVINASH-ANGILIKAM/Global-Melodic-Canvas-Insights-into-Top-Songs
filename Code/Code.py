# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read data from CSV
df = pd.read_csv('https://raw.githubusercontent.com/AVINASH-ANGILIKAM/Global-Melodic-Canvas-Insights-into-Top-Songs/main/Data%20Set/Song.csv')
df.head()

# Check for duplicate rows
duplicate_rows = df.duplicated()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Display information about the DataFrame
df.info()

# Display basic statistics of the DataFrame
df.describe()

# Select only numeric columns
numeric_columns = df.select_dtypes(include=['number'])

# Calculate mean, median, standard deviation, skewness, and kurtosis
statistics = numeric_columns.agg(['mean', 'median', 'std', 'skew', 'kurt'])

# Compute the correlation matrix
correlation_matrix = numeric_columns.corr()

# Get basic statistics using describe()
basic_statistics = numeric_columns.describe()

# Print the results
print("Mean, Median, Standard Deviation, Skewness, Kurtosis:")
print(statistics)

print("\nCorrelation Matrix:")
print(correlation_matrix)

print("\nBasic Statistics:")
print(basic_statistics)

# Find top 50 artists by maximum sales
top_50 = max_sales_per_artist.sort_values(by='Sales', ascending=False).head(50)

# Find the maximum sales value for each artist
max_sales_per_artist = df.groupby('Artist')['Sales'].max().reset_index()

plt.figure(figsize=(16, 12))
plt.bar(top_50['Artist'], top_50['Sales'], color='lightgreen', edgecolor='black')
plt.title('Top 50 Artists by Sales')
plt.xlabel('Artist')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# Filter data up to 2014 and plot line chart of sales, streams, downloads, and radio plays
df_up_to_2014 = df[df['Year'] <= 2014]
sales_streams_downloads_radio_plays_by_year = df_up_to_2014.groupby('Year')[['Sales', 'Streams', 'Downloads', 'Radio Plays']].sum()

plt.figure(figsize=(12, 8))
sales_streams_downloads_radio_plays_by_year.plot(kind='line')
plt.title('Sales, Streams, Downloads, and Radio Plays Up to 2014')
plt.xlabel('Year')
plt.ylabel('Quantile')
plt.grid(True)
plt.xticks(range(1900, 2020, 5), rotation=45)
plt.legend(title='Variables')
plt.tight_layout()
plt.show()

# Plot correlation heatmap
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
