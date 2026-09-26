-- Retail Banking Customer Churn Analysis
-- Business-oriented SQL queries for portfolio monitoring.

-- 1. Overall churn KPI
SELECT
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(100.0 * AVG(Churn), 2) AS churn_rate_pct
FROM customers;

-- 2. Geographic churn
SELECT Geography,
       COUNT(*) AS customers,
       ROUND(100.0 * AVG(Churn), 2) AS churn_rate_pct,
       ROUND(AVG(Balance), 2) AS avg_balance
FROM customers
GROUP BY Geography
ORDER BY churn_rate_pct DESC;

-- 3. Active vs inactive customers
SELECT IsActiveMember,
       COUNT(*) AS customers,
       ROUND(100.0 * AVG(Churn), 2) AS churn_rate_pct
FROM customers
GROUP BY IsActiveMember
ORDER BY churn_rate_pct DESC;

-- 4. Product holdings
SELECT NumOfProducts,
       COUNT(*) AS customers,
       ROUND(100.0 * AVG(Churn), 2) AS churn_rate_pct,
       ROUND(AVG(Balance), 2) AS avg_balance
FROM customers
GROUP BY NumOfProducts
ORDER BY NumOfProducts;

-- 5. Higher-balance customers at risk
SELECT Geography,
       COUNT(*) AS churned_high_balance_customers,
       ROUND(AVG(Balance), 2) AS avg_balance
FROM customers
WHERE Churn = 1 AND Balance >= 100000
GROUP BY Geography
ORDER BY churned_high_balance_customers DESC;

-- 6. Age segmentation
SELECT
    CASE
        WHEN Age < 30 THEN 'Under 30'
        WHEN Age <= 45 THEN '30-45'
        WHEN Age <= 60 THEN '46-60'
        ELSE '60+'
    END AS age_segment,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(Churn), 2) AS churn_rate_pct
FROM customers
GROUP BY age_segment
ORDER BY churn_rate_pct DESC;
