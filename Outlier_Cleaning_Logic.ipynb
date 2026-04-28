import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load your uploaded dataset
# Make sure the file 'used_cars.csv' is in the same folder as your code
df = pd.read_csv('used_cars.csv')

# 2. Data Cleaning: Convert 'price' from text ($10,300) to numbers (10300)
# This is a crucial step in real-world Machine Learning
df['price_numeric'] = df['price'].str.replace('$', '').str.replace(',', '').astype(float)

# 3. Set up the Visualization Canvas
plt.figure(figsize=(12, 5))

# --- Plot 1: Before Cleaning ---
plt.subplot(1, 2, 1)
sns.boxplot(x=df['price_numeric'], color='red')
plt.title('Before Outlier Removal (Black Diamonds are outliers)')
plt.xlabel('Price in USD')

# 4. Outlier Detection Logic (IQR Method)
Q1 = df['price_numeric'].quantile(0.25)
Q3 = df['price_numeric'].quantile(0.75)
IQR = Q3 - Q1

# Defining boundaries
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# 5. Data Filtering
# Removing outliers to get a cleaner dataset
df_clean = df[(df['price_numeric'] >= lower_bound) & (df['price_numeric'] <= upper_bound)]

# --- Plot 2: After Cleaning ---
plt.subplot(1, 2, 2)
sns.boxplot(x=df_clean['price_numeric'], color='green')
plt.title('After Removal of Outliers (Clean Data)')
plt.xlabel('Price in USD')

plt.tight_layout()
plt.show()

# Print how many outliers were removed
print(f"Total cars in original data: {len(df)}")
print(f"Total cars after cleaning: {len(df_clean)}")
print(f"Total outliers removed: {len(df) - len(df_clean)}")
