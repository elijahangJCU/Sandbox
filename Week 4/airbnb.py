import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Step 1: Load dataset
df = pd.read_csv("sg_listings_cleaned.csv")

# Step 2: Basic exploration
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nInfo:")
print(df.info())
print("\nDescription:")
print(df.describe())
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 3: Clean data
df_clean = df.dropna(subset=['last_review'])
df_clean = df_clean[df_clean['price'] <= 1000]

# Step 4: Visualizations

# Histogram of prices
plt.figure(figsize=(10,6))
sns.histplot(df_clean['price'], bins=50, kde=False)
plt.title('Histogram of Prices')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

# Boxplot of price by room_type
plt.figure(figsize=(10,6))
sns.boxplot(x='room_type', y='price', data=df_clean)
plt.title('Boxplot of Price by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.show()

# Time series analysis
df_clean['last_review'] = pd.to_datetime(df_clean['last_review'])
df_clean['quarter'] = df_clean['last_review'].dt.to_period('Q')
availability_by_quarter = df_clean.groupby('quarter')['availability_365'].mean().reset_index()
availability_by_quarter['quarter'] = availability_by_quarter['quarter'].astype(str)

plt.figure(figsize=(12,6))
sns.lineplot(data=availability_by_quarter, x='quarter', y='availability_365', marker='o')
plt.title('Average Availability (365 days) by Quarter')
plt.xlabel('Quarter')
plt.ylabel('Average Availability')
plt.xticks(rotation=45)
plt.show()

# Step 5: Statistical test - t-test comparing price of entire home vs private room
entire_home_prices = df_clean[df_clean['room_type'] == 'Entire home/apt']['price']
private_room_prices = df_clean[df_clean['room_type'] == 'Private room']['price']
t_stat, p_val = ttest_ind(entire_home_prices, private_room_prices, equal_var=False)
print(f"T-test comparing prices between Entire home/apt and Private room:")
print(f"t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")

# Step 6: Machine learning - Linear Regression predicting price
features = ['minimum_nights', 'number_of_reviews']
X = df_clean[features]
y = df_clean['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print("\nLinear Regression Model:")
print(f"Coefficients: {dict(zip(features, model.coef_))}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"R^2 score on test set: {r2:.4f}")
