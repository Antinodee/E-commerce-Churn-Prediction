# E-commerce Customer Analytics & Churn Prediction

## Dataset: UCI Online Retail (Public Dataset)

**Source:** UCI Machine Learning Repository  
**Link:** https://www.kaggle.com/datasets/vijayuv/onlineretail

### Citation
```
Daqing Chen, Sai Liang Sain, and Kun Guo
Data mining for the online retail industry: A case study of RFM model-based 
customer segmentation using data mining
Journal of Database Marketing and Customer Strategy Management, 
Vol. 19, No. 3, pp. 197-208, 2012
```

## Dataset Statistics
- **397,884 transactions** from UK online retailer
- **4,338 unique customers** across 37 countries
- **3,665 unique products**
- **$8.9M total revenue** (Dec 2010 - Dec 2011)
- **33.3% churn rate**

## Project Features
✅ Customer RFM Segmentation (6 segments)  
✅ Churn Prediction with 100% accuracy  
✅ SQL Analytics  
✅ Interactive Dashboard (Streamlit)

## Key Results
- **Champions:** 1,261 customers ($5,421 avg LTV)
- **At Risk:** 245 customers (76.7% churn rate)
- **Top Features:** Recency (82.6%), Customer Lifetime (6.2%)

## Files
- `process_data.py` - Data processing pipeline
- `customers.csv` - Customer analytics (4,338 records)
- `transactions.csv` - Transaction data (397K records)
- `churn_model.pkl` - Trained ML model
- `ecommerce.db` - SQLite database

## How to Use
1. Download UCI dataset from Kaggle
2. Run: `python process_data.py`
3. Run: `python train_model.py`

**License:** Public dataset for research/education
