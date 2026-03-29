import sqlite3
import pandas as pd

conn = sqlite3.connect('ecommerce.db')

print("📊 SQL ANALYTICS\n")

# Query 1: Revenue by Country
print("\n1️⃣ Top 10 Countries by Revenue:")
query = """
SELECT Country, 
       COUNT(DISTINCT CustomerID) as Customers,
       ROUND(SUM(TotalSpent), 2) as Revenue
FROM customers
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10
"""
print(pd.read_sql_query(query, conn))

# Query 2: High-risk customers
print("\n2️⃣ High-Risk Customers (At Risk + Lost):")
query2 = """
SELECT Segment, 
       COUNT(*) as Count,
       ROUND(AVG(TotalSpent), 2) as AvgLTV,
       ROUND(AVG(RecencyDays), 0) as AvgRecency
FROM customers
WHERE Segment IN ('At Risk', 'Lost')
GROUP BY Segment
"""
print(pd.read_sql_query(query2, conn))

conn.close()