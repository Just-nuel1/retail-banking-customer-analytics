# Retail Banking Customer Churn & Retention Analytics

**Python · SQL · Statistical Analysis · Machine Learning · Business Analytics**

An end-to-end portfolio project analyzing customer attrition in a retail-banking setting and translating customer data into decision-relevant retention insights.

## Business Problem

Customer attrition can reduce customer lifetime value and increase acquisition costs. This project asks:

> **Which customer characteristics are associated with churn, can we identify customers at elevated churn risk, and how could those insights support a targeted retention strategy?**

## Dataset

The project uses a **public dataset of 10,000 retail-banking customers** across France, Germany and Spain. It contains credit score, geography, gender, age, tenure, balance, product holdings, credit-card ownership, activity status, estimated salary and churn outcome.

This is a portfolio project using public data. **It is not RBC data and is not affiliated with or endorsed by RBC.**

## Analytical Workflow

1. **Data quality review** — missing values, duplicates, types and field usability
2. **Exploratory analysis** — portfolio churn KPI and customer segmentation
3. **SQL analysis** — churn, balances, activity, products and age segments
4. **Feature engineering** — stakeholder-friendly segments and model-ready transformations
5. **Machine learning** — interpretable logistic-regression baseline
6. **Evaluation** — precision, recall, F1, confusion matrix and ROC-AUC
7. **Business translation** — turn analytical signals into retention hypotheses and monitoring recommendations

## Key Portfolio Findings

The dataset contains **2,037 churned customers out of 10,000 (20.37%)**.

Published analyses of the same dataset show several notable associations:
- Germany has a substantially higher churn rate than France and Spain.
- Inactive members churn considerably more often than active members.
- Churn varies strongly across age and number-of-products segments.
- These are **associations, not causal conclusions**; they identify areas for deeper investigation.

The included notebook reproduces the portfolio analysis directly from the public source and trains the model from scratch.

## Why Accuracy Alone Is Not Enough

Only about one-fifth of the portfolio churns. A model can therefore appear accurate while doing a poor job identifying the customers the business cares about. This project evaluates **precision, recall, F1 and ROC-AUC** in addition to the confusion matrix.

## Repository Structure

    retail-banking-customer-analytics/
    ├── README.md
    ├── analysis/
    │   └── customer_churn_analysis.py
    ├── notebooks/
    │   └── customer_churn_analysis.ipynb
    ├── sql/
    │   └── customer_analysis.sql
    ├── reports/
    │   └── executive_summary.md
    └── requirements.txt

## Business Recommendations

- Investigate elevated-churn segments to determine whether engagement, service, pricing or product experience explains observed differences.
- Treat inactivity as an engagement signal worth monitoring and test targeted re-engagement strategies.
- Prioritize retention using **churn risk together with customer value**, rather than targeting every predicted churner equally.
- Track churn KPIs by customer segment over time and evaluate retention initiatives through controlled testing.

## Limitations

This public portfolio dataset does not include transaction histories, customer interactions, profitability, campaign exposure or longitudinal behaviour. The model demonstrates an analytical workflow; it is **not a production banking decision system**. Demographic variables require additional governance and fairness review in any real-world application.

## Skills Demonstrated

Python · pandas · NumPy · SQL · scikit-learn · EDA · Data Quality · Feature Engineering · Classification · Model Evaluation · Business Intelligence · Stakeholder Communication

## Author

**Emmanuel Odinamba**  
BSc Mathematics & Economics, Minor in Statistics — University of Prince Edward Island  
GitHub: **@Just-nuel1**
