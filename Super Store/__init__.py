# Global Superstore Orders 2016 Analysis and Visualization Script

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot styles
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 2. Load the dataset (with encoding fix)
import os
file_path = os.path.join(os.path.dirname(__file__), 'Global Superstore Orders 2016.csv')
df = pd.read_csv(file_path, encoding='latin1')

# 3. Data cleaning
# Convert Order Date and Ship Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce', dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce', dayfirst=True)

# Drop rows with missing values in critical columns
df.dropna(subset=['Order Date', 'Sales', 'Profit', 'Region', 'Category', 'Segment'], inplace=True)

# Strip whitespace from string columns to avoid key errors
str_cols = df.select_dtypes(include='object').columns
for col in str_cols:
    df[col] = df[col].str.strip()

# 4. Feature engineering
# Create YearMonth feature for time-series analysis
df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)

# Calculate Profit Margin as Profit divided by Sales
df['Profit Margin'] = df['Profit'] / df['Sales']

# 5. Exploratory analysis
# Total Sales and Profit by Region
region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()

# Sales by Region and Category
region_category_sales = df.groupby(['Region', 'Category'])['Sales'].sum().reset_index()

# Profit by Segment and Region
segment_region_profit = df.groupby(['Segment', 'Region'])['Profit'].sum().reset_index()

# Sales trends by Region over time
region_time_sales = df.groupby(['YearMonth', 'Region'])['Sales'].sum().reset_index()

# Sales trends by Segment and Category over time
segment_category_time_sales = df.groupby(['YearMonth', 'Segment', 'Category'])['Sales'].sum().reset_index()

# 6. Visualizations

# Regional Sales and Profit (side-by-side bar plot)
region_summary_sorted = region_summary.sort_values('Sales', ascending=False)
# Convert Sales and Profit to millions
region_summary_sorted['Sales'] = region_summary_sorted['Sales'] / 1e6
region_summary_sorted['Profit'] = region_summary_sorted['Profit'] / 1e6
# Define Profit_Status
avg_profit = region_summary_sorted['Profit'].mean()
region_summary_sorted['Profit_Status'] = region_summary_sorted['Profit'].apply(
    lambda x: 'High' if x > avg_profit * 1.1 else ('Low' if x < avg_profit * 0.9 else 'Normal')
)

fig, ax = plt.subplots()
bars = ax.bar(region_summary_sorted['Region'], region_summary_sorted['Sales'], label='Sales', color='#1f77b4')
for i, val in enumerate(region_summary_sorted['Profit']):
    color = '#2ca02c' if region_summary_sorted['Profit_Status'].iloc[i] == 'High' else (
        '#d62728' if region_summary_sorted['Profit_Status'].iloc[i] == 'Low' else '#cc7a00')
    ax.bar(region_summary_sorted['Region'].iloc[i], val, label='_nolegend_', color=color, width=0.4, alpha=0.9)

ax.set_xlabel('Region')
ax.set_ylabel('Amount (in millions)')
ax.set_title('Total Sales and Profit by Region')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
# Custom legend explaining profit color meanings
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2ca02c', label='🟩 High: Profit > 110% of average profit'),
    Patch(facecolor='#cc7a00', label='🟧 Normal: 90% ≤ Profit ≤ 110% of average profit'),
    Patch(facecolor='#d62728', label='🟥 Low: Profit < 90% of average profit'),
    Patch(facecolor='#1f77b4', label='Sales (in millions)')
]
ax.legend(handles=legend_elements, title='Category Meaning', loc='upper right', frameon=True)
# plt.legend(['Sales', 'Profit'])  # old legend removed/commented out
plt.show()

# Sales Trends by Region (line plot)
plt.figure()
sns.lineplot(data=region_time_sales, x='YearMonth', y='Sales', hue='Region', marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Sales Trends by Region')
plt.xlabel('Year-Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Sales by Product Category per Region (grouped bar plot)
plt.figure()
sns.barplot(data=region_category_sales, x='Region', y='Sales', hue='Category')
plt.title('Sales by Product Category per Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.legend(title='Category')
plt.tight_layout()
plt.show()

# Profit by Segment across Regions (grouped bar plot)
plt.figure()
sns.barplot(data=segment_region_profit, x='Region', y='Profit', hue='Segment')
plt.title('Profit by Segment across Regions')
plt.xlabel('Region')
plt.ylabel('Profit')
plt.legend(title='Segment')
plt.tight_layout()
plt.show()

# Sales Trends by Segment & Category (multi-line plot)
plt.figure()
for (segment, category), group_data in segment_category_time_sales.groupby(['Segment', 'Category']):
    plt.plot(group_data['YearMonth'], group_data['Sales'], label=f'{segment} - {category}', marker='o')

plt.xticks(rotation=45)
plt.title('Sales Trends by Segment & Category')
plt.xlabel('Year-Month')
plt.ylabel('Sales')
plt.legend(title='Segment - Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
