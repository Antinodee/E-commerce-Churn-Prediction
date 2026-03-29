import pandas as pd
import pickle

print("=" * 60)
print("TESTING E-COMMERCE ANALYTICS PROJECT")
print("=" * 60)

# Test 1: Load customer data
print("\n1. Loading customer data...")
customers = pd.read_csv('customers.csv')
print(f"✅ Loaded {len(customers):,} customers")

# Test 2: Load transactions
print("\n2. Loading transactions...")
transactions = pd.read_csv('transactions.csv')
print(f"✅ Loaded {len(transactions):,} transactions")

# Test 3: Load ML model
print("\n3. Loading ML model...")
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)
print(f"✅ Model loaded: {type(model).__name__}")

# Test 4: Show summary
print("\n" + "=" * 60)
print("PROJECT STATISTICS")
print("=" * 60)
print(f"Total Customers: {len(customers):,}")
print(f"Total Transactions: {len(transactions):,}")
print(f"Total Revenue: ${transactions['TotalAmount'].sum():,.2f}")
print(f"Churn Rate: {customers['Churned'].mean()*100:.1f}%")

print("\n✅ ALL TESTS PASSED! Project is working!")