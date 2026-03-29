# 🛍️ E-commerce Customer Churn Prediction

Advanced customer analytics and churn prediction system using the UCI Online Retail dataset with RFM segmentation and Random Forest machine learning.

## 📊 Project Overview

This project analyzes **397,884 real transactions** from a UK-based online retailer to predict customer churn and provide actionable business insights. Using RFM (Recency, Frequency, Monetary) segmentation and machine learning, the system identifies at-risk customers and recommends targeted retention strategies.

## 📈 Dataset

**Source:** UCI Machine Learning Repository - Online Retail Dataset  
**Link:** https://www.kaggle.com/datasets/vijayuv/onlineretail

### Dataset Statistics:
- **Transactions:** 397,884 (cleaned from 541,909 original)
- **Customers:** 4,338 unique customers
- **Products:** 3,665 unique items
- **Countries:** 37 countries
- **Revenue:** $8,911,407.90
- **Time Period:** December 2010 - December 2011
- **License:** Public domain (academic use)

### Data Cleaning Process:
- Removed cancelled orders (InvoiceNo starting with 'C')
- Filtered invalid/negative quantities
- Handled missing customer IDs
- Removed outlier prices

## 🎯 Key Features

### 1. RFM Customer Segmentation
Classified customers into 6 actionable segments:
- **Champions** (1,261 customers) - High value, recent purchasers
- **Loyal Customers** (841 customers) - Regular repeat buyers
- **At Risk** (245 customers) - Previously valuable, now inactive
- **Lost** (1,503 customers) - Haven't purchased recently
- **New Customers** (108 customers) - First-time buyers
- **Potential** (380 customers) - Moderate activity

### 2. Churn Prediction Model
- **Algorithm:** Random Forest Classifier
- **Accuracy:** 100% on test set
- **Top Feature:** Recency (82.6% importance)
- **Features Used:** 7 customer behavior metrics

### 3. Business Intelligence Analytics
- SQL-based customer insights
- Revenue analysis by segment and country
- Retention recommendations
- Customer lifetime value (LTV) calculations

## 📊 Key Results

| Metric | Value |
|--------|-------|
| Overall Churn Rate | 33.3% |
| Champions Avg LTV | $5,421 |
| At-Risk Customers | 245 (76.7% churn rate) |
| Top Revenue Country | United Kingdom ($7.2M) |
| Most Important Feature | Recency (82.6%) |

### Business Insights:
1. **Recency is the strongest churn predictor** - Customers inactive for 90+ days have 76% churn probability
2. **Champions generate majority revenue** - Top 20% of customers contribute 60%+ of revenue
3. **245 At-Risk customers** need immediate retention campaigns
4. **Lost segment** (1,503 customers) represents significant re-engagement opportunity

## 🛠️ Technologies Used

**Programming & Libraries:**
- Python 3.8+
- pandas (data manipulation)
- NumPy (numerical computing)
- scikit-learn (machine learning)
- SQLite (database)

**Analysis Techniques:**
- RFM Analysis
- Random Forest Classification
- Customer Segmentation
- SQL Analytics
- Feature Engineering

## 🚀 How to Run

### Installation:
```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Run the Project:

**1. Main Demo (Recommended):**
```bash
python demo.py
```
Shows complete project statistics, customer segments, and business insights.

**2. Customer Segment Analysis:**
```bash
python analysis1.py
```
Deep dive into each customer segment with detailed metrics.

**3. SQL Analytics:**
```bash
python analysis2.py
```
Advanced SQL queries on revenue, churn rates, and geographic distribution.

**4. Data Processing (Optional):**
```bash
python process_data.py
```
Re-runs the complete ETL pipeline from raw data.

## 📁 Project Structure

```
ecommerce-churn-prediction/
├── demo.py                 # Main project demo
├── analysis1.py            # Customer segment deep dive
├── analysis2.py            # SQL analytics queries
├── process_data.py         # Data processing pipeline
├── customers.csv           # Processed customer data (4,338 rows)
├── transactions.csv        # Transaction data (397,884 rows)
├── churn_model.pkl         # Trained ML model
├── ecommerce.db           # SQLite database
└── README.md              # This file
```

## 💡 Sample Output

```
======================================================================
E-COMMERCE CUSTOMER ANALYTICS - PROJECT DEMO
======================================================================

📊 Dataset Statistics:
   Total Customers: 4,338
   Total Transactions: 397,884
   Total Revenue: $8,911,407.90

👥 Customer Segmentation:
   Champions: 1,261 customers (Avg LTV: $5,421.45)
   At Risk: 245 customers (Avg LTV: $3,187.23)
   Lost: 1,503 customers (Avg LTV: $1,892.15)

⚠️  Churn Analysis:
   Total Churned: 1,445 (33.3%)
   At Risk: 245 customers
   Recommendation: Immediate retention campaign needed
```

## 🎓 Skills Demonstrated

### Data Science:
- Customer analytics and segmentation
- Predictive modeling (churn prediction)
- Feature engineering
- Model evaluation and interpretation

### Data Engineering:
- ETL pipeline development
- Data cleaning and validation
- Database design (SQLite)
- Large dataset processing (400K+ rows)

### Business Intelligence:
- RFM analysis methodology
- Customer lifetime value calculation
- Actionable business insights
- Retention strategy recommendations

### Technical Skills:
- Python programming
- SQL queries
- Machine learning (Random Forest)
- Data visualization concepts

## 📈 Use Cases

1. **Customer Retention:** Identify at-risk customers before they churn
2. **Marketing Campaigns:** Target specific segments with personalized offers
3. **Revenue Optimization:** Focus resources on high-value Champions
4. **Re-engagement:** Win back Lost customers with tailored incentives
5. **Business Intelligence:** Track customer health metrics over time

## 🔮 Future Enhancements

- [ ] Deploy as REST API using Flask
- [ ] Add time-series forecasting for churn prediction
- [ ] Implement A/B testing framework for retention strategies
- [ ] Create interactive dashboard (Tableau/Power BI)
- [ ] Add customer cohort analysis
- [ ] Integrate with CRM systems

## 📚 Academic Citation

The UCI Online Retail dataset used in this project is cited in:

```
Chen, D., Sain, S.L., and Guo, K. (2012)
"Data mining for the online retail industry: A case study of RFM model-based 
customer segmentation using data mining"
Journal of Database Marketing & Customer Strategy Management
Vol. 19, No. 3, pp. 197-208
```

## 👤 Author

**Rajeev Pernapati**
- MS Computer Science, University of Nevada, Las Vegas
- Email: rajeev30403@gmail.com
- LinkedIn: [Your LinkedIn URL]
- Portfolio: [Your Portfolio URL]

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the dataset
- Kaggle community for data accessibility
- scikit-learn for machine learning tools

---

**⭐ If you found this project useful, please consider giving it a star!**
