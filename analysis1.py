import pandas as pd

customers = pd.read_csv('customers.csv')

print("🎯 CUSTOMER SEGMENT DEEP DIVE\n")

for segment in customers['Segment'].unique():
    seg_data = customers[customers['Segment'] == segment]
    print(f"\n{'='*60}")
    print(f"{segment.upper()}")
    print(f"{'='*60}")
    print(f"  Customers: {len(seg_data)}")
    print(f"  Avg Spent: ${seg_data['TotalSpent'].mean():,.2f}")
    print(f"  Avg Orders: {seg_data['TotalOrders'].mean():.1f}")
    print(f"  Churn Rate: {seg_data['Churned'].mean()*100:.1f}%")
    print(f"  Top Country: {seg_data['Country'].mode().values[0]}")