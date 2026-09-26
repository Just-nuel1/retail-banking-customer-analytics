# Executive Summary

## Objective
Identify customer segments associated with elevated attrition and build an interpretable baseline model for churn-risk analysis.

## Dataset
Public retail-banking churn dataset with 10,000 customer records across France, Germany and Spain. The dataset is used for portfolio demonstration only and is not RBC data.

## Initial Findings
Published summaries of this dataset report an overall churn rate of **20.37% (2,037 of 10,000 customers)**. Germany has a materially higher churn rate than France and Spain, and inactive customers show substantially higher attrition than active customers.

These observations are treated as **associations**, not proof that geography, age, gender, or any other attribute causes churn.

## Analytical Approach
- Validate data completeness and duplicates.
- Analyze churn across customer segments using Python and SQL.
- Engineer stakeholder-friendly age segments.
- Encode categorical variables and standardize numerical variables.
- Use a stratified train/test split.
- Fit an interpretable logistic-regression baseline with class weighting.
- Evaluate with precision, recall, F1 and ROC-AUC rather than accuracy alone.
- Generate customer-level risk probabilities for prioritization analysis.

## Business Recommendations
1. Investigate high-churn segments to determine whether service, pricing, engagement or product-experience factors explain the observed differences.
2. Use activity status as an early engagement signal and test targeted re-engagement interventions.
3. Prioritize retention resources using both churn probability and customer value rather than churn probability alone.
4. Track churn KPIs by segment over time and validate interventions through controlled testing.

## Limitations
This is a public portfolio dataset and does not contain transaction histories, customer interactions, product profitability or time-series behaviour. The model therefore demonstrates analytical workflow rather than production banking performance. Model outputs should not be used for real customer decisions.
