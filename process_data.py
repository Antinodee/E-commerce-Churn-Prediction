"""
E-commerce Customer Analytics & Churn Prediction
Using UCI ONLINE RETAIL PUBLIC DATASET

Dataset: UCI Machine Learning Repository - Online Retail Dataset
Source: https://www.kaggle.com/datasets/vijayuv/onlineretail
Citation: Chen, D., Sain, S.L., Guo, K. (2012)
         Data mining for the online retail industry: A case study of RFM model-based 
         customer segmentation using data mining,
         Journal of Database Marketing and Customer Strategy Management

This script processes the UCI Online Retail dataset for customer analytics and churn prediction.
"""
import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3

print("=" * 80)
print("UCI ONLINE RETAIL DATASET - DATA PROCESSING")
print("=" * 80)

# Load dataset
print("\n📥 Loading UCI Online Retail Dataset...")
df = pd.read_csv('/tmp/OnlineRetail.csv', encoding='ISO-8859-1')

print(f"\n✅ Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")

# Data Cleaning
print("\n" + "=" * 80)
print("DATA CLEANING")
print("=" * 80)

initial_count = len(df)

# Remove cancelled orders (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
print(f"✅ Removed {initial_count - len(df):,} cancelled orders")

# Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])
print(f"✅ Removed rows with missing CustomerID - {len(df):,} rows remaining")

# Remove negative/zero quantities and prices
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
print(f"✅ Removed invalid quantities/prices - {len(df):,} rows remaining")

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Calculate Total Amount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Convert CustomerID to integer
df['CustomerID'] = df['CustomerID'].astype(int)

print(f"\n📊 Clean Dataset Statistics:")
print(f"- Total Transactions: {len(df):,}")
print(f"- Unique Customers: {df['CustomerID'].nunique():,}")
print(f"- Unique Products: {df['StockCode'].nunique():,}")
print(f"- Countries: {df['Country'].nunique()}")
print(f"- Total Revenue: ${df['TotalAmount'].sum():,.2f}")
print(f"- Date Range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")

# Country distribution
print(f"\nTop 10 Countries by Revenue:")
country_revenue = df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)
for country, revenue in country_revenue.items():
    print(f"  {country}: ${revenue:,.2f}")

# Create Customer Analytics Dataset
print("\n" + "=" * 80)
print("CREATING CUSTOMER ANALYTICS DATASET")
print("=" * 80)

# Calculate customer metrics
customer_data = df.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',  # Number of orders
    'TotalAmount': 'sum',     # Total spent
    'InvoiceDate': ['min', 'max'],  # First and last purchase
    'Quantity': 'sum',        # Total items purchased
    'Country': 'first'        # Customer country
}).reset_index()

# Flatten column names
customer_data.columns = ['CustomerID', 'TotalOrders', 'TotalSpent', 'FirstPurchase', 
                          'LastPurchase', 'TotalItems', 'Country']

# Calculate recency (days since last purchase from dataset end date)
max_date = df['InvoiceDate'].max()
customer_data['RecencyDays'] = (max_date - customer_data['LastPurchase']).dt.days

# Calculate average order value
customer_data['AvgOrderValue'] = customer_data['TotalSpent'] / customer_data['TotalOrders']

# Calculate customer lifetime (days between first and last purchase)
customer_data['CustomerLifetimeDays'] = (customer_data['LastPurchase'] - customer_data['FirstPurchase']).dt.days

# Calculate purchase frequency (orders per month)
customer_data['OrdersPerMonth'] = customer_data['TotalOrders'] / (customer_data['CustomerLifetimeDays'] / 30 + 1)

# Determine churn (if last purchase was more than 90 days before dataset end)
customer_data['Churned'] = (customer_data['RecencyDays'] > 90).astype(int)

# Assign customer segments using rank-based RFM scoring
# This handles duplicate values better than qcut
customer_data['RecencyScore'] = pd.cut(customer_data['RecencyDays'].rank(method='first'), bins=4, labels=[4, 3, 2, 1])
customer_data['FrequencyScore'] = pd.cut(customer_data['TotalOrders'].rank(method='first'), bins=4, labels=[1, 2, 3, 4])
customer_data['MonetaryScore'] = pd.cut(customer_data['TotalSpent'].rank(method='first'), bins=4, labels=[1, 2, 3, 4])

# Create RFM Score
customer_data['RFM_Score'] = (customer_data['RecencyScore'].astype(int) + 
                                customer_data['FrequencyScore'].astype(int) + 
                                customer_data['MonetaryScore'].astype(int))

# Segment customers
def assign_segment(row):
    if row['RFM_Score'] >= 10:
        return 'Champions'
    elif row['RFM_Score'] >= 8:
        return 'Loyal Customers'
    elif row['RecencyScore'] == 4 and row['FrequencyScore'] <= 2:
        return 'New Customers'
    elif row['RecencyScore'] <= 2 and row['FrequencyScore'] >= 3:
        return 'At Risk'
    elif row['RecencyScore'] <= 2 and row['FrequencyScore'] <= 2:
        return 'Lost'
    else:
        return 'Potential'

customer_data['Segment'] = customer_data.apply(assign_segment, axis=1)

print(f"\n✅ Customer analytics dataset created!")
print(f"Total Customers: {len(customer_data):,}")
print(f"Churn Rate: {customer_data['Churned'].mean()*100:.1f}%")

print(f"\nCustomer Segments:")
print(customer_data['Segment'].value_counts())

print(f"\nSegment Performance:")
segment_stats = customer_data.groupby('Segment').agg({
    'CustomerID': 'count',
    'TotalSpent': 'mean',
    'TotalOrders': 'mean',
    'Churned': 'mean'
})
segment_stats.columns = ['Customers', 'Avg LTV', 'Avg Orders', 'Churn Rate']
segment_stats['Churn Rate'] = (segment_stats['Churn Rate'] * 100).round(1)
segment_stats['Avg LTV'] = segment_stats['Avg LTV'].round(2)
segment_stats['Avg Orders'] = segment_stats['Avg Orders'].round(1)
print(segment_stats.to_string())

# Save datasets
print("\n" + "=" * 80)
print("SAVING DATASETS")
print("=" * 80)

# Save transaction data
df.to_csv('/home/claude/projects/ecommerce-analytics-public/transactions.csv', index=False)
print("✅ Saved: transactions.csv ({:,} rows)".format(len(df)))

# Save customer data
customer_data.to_csv('/home/claude/projects/ecommerce-analytics-public/customers.csv', index=False)
print("✅ Saved: customers.csv ({:,} rows)".format(len(customer_data)))

# Create SQLite database
print("\n📊 Creating SQLite Database...")
conn = sqlite3.connect('/home/claude/projects/ecommerce-analytics-public/ecommerce.db')

df.to_sql('transactions', conn, if_exists='replace', index=False)
customer_data.to_sql('customers', conn, if_exists='replace', index=False)

conn.close()
print("✅ Saved: ecommerce.db")

# Print summary
print("\n" + "=" * 80)
print("SUMMARY - UCI ONLINE RETAIL DATASET")
print("=" * 80)

print(f"""
Dataset Information:
- Source: UCI Machine Learning Repository
- Real-world data: UK-based online retailer (Dec 2010 - Dec 2011)
- Transactions: {len(df):,}
- Customers: {len(customer_data):,}
- Products: {df['StockCode'].nunique():,}
- Countries: {df['Country'].nunique()}
- Total Revenue: ${df['TotalAmount'].sum():,.2f}

Customer Analytics:
- Churn Rate: {customer_data['Churned'].mean()*100:.1f}%
- Champions: {len(customer_data[customer_data['Segment'] == 'Champions']):,}
- At Risk: {len(customer_data[customer_data['Segment'] == 'At Risk']):,}
- Lost Customers: {len(customer_data[customer_data['Segment'] == 'Lost']):,}

Files Created:
✅ transactions.csv - All cleaned transactions
✅ customers.csv - Customer-level analytics with RFM segmentation
✅ ecommerce.db - SQLite database

Citation:
Chen, D., Sain, S.L., Guo, K. (2012)
Data mining for the online retail industry: A case study of RFM model-based 
customer segmentation using data mining,
Journal of Database Marketing and Customer Strategy Management, Vol. 19, No. 3, pp. 197-208
""")

print("=" * 80)
print("✅ DATA PROCESSING COMPLETE!")
print("=" * 80)
print("\nNext steps:")
print("1. Run: python sql_analysis.py (SQL analytics)")
print("2. Run: python train_model.py (ML churn prediction)")
print("3. Run: streamlit run dashboard.py (interactive dashboard)")
