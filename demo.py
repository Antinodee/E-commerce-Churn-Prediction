import pandas as pd

print("=" * 70)
print("E-COMMERCE CUSTOMER ANALYTICS - PROJECT DEMO")
print("=" * 70)

# Load data
customers = pd.read_csv('customers.csv')
transactions = pd.read_csv('transactions.csv')

# Statistics
print(f"\n📊 Dataset Statistics:")
print(f"   Total Customers: {len(customers):,}")
print(f"   Total Transactions: {len(transactions):,}")
print(f"   Total Revenue: ${transactions['TotalAmount'].sum():,.2f}")

# Segments
print(f"\n👥 Customer Segmentation:")
segments = customers.groupby('Segment').agg({
    'CustomerID': 'count',
    'TotalSpent': 'mean',
    'Churned': lambda x: x.mean() * 100
}).round(2)
segments.columns = ['Count', 'Avg LTV ($)', 'Churn Rate (%)']
print(segments.sort_values('Avg LTV ($)', ascending=False))

# Top customers
print(f"\n🏆 Top 10 Customers by Spending:")
top10 = customers.nlargest(10, 'TotalSpent')[['CustomerID', 'TotalSpent', 'TotalOrders', 'Segment', 'Country']]
print(top10.to_string(index=False))

# At-risk customers
at_risk = customers[customers['Segment'] == 'At Risk']
print(f"\n⚠️  At-Risk Customers: {len(at_risk)}")
print(f"   Average LTV: ${at_risk['TotalSpent'].mean():,.2f}")
print(f"   Churn Rate: {at_risk['Churned'].mean()*100:.1f}%")

print("\n✅ PROJECT DATA LOADED SUCCESSFULLY!")
print("\nNote: ML model functionality available - just needs environment setup.")