"""
Retail Banking Customer Churn & Retention Analytics
Author: Emmanuel Odinamba

Reproducible end-to-end analysis using public banking churn data.
Run in Google Colab, Jupyter, or a local Python environment.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_auc_score,
    RocCurveDisplay, ConfusionMatrixDisplay
)

DATA_URL = "https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Bank%20Churn%20Modelling.csv"

# 1. LOAD DATA
df = pd.read_csv(DATA_URL)
print("Dataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst five rows:")
print(df.head())

# 2. DATA QUALITY REVIEW
print("\n--- DATA QUALITY ---")
print("Missing values:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
print("\nData types:")
print(df.dtypes)

# Standardize column names for easier analysis/SQL.
df = df.rename(columns={
    "Num Of Products": "NumOfProducts",
    "Has Credit Card": "HasCreditCard",
    "Is Active Member": "IsActiveMember",
    "Estimated Salary": "EstimatedSalary"
})

# IDs/names are not useful predictive features.
model_df = df.drop(columns=["CustomerId", "Surname"], errors="ignore").copy()

# 3. EXPLORATORY ANALYSIS
churn_rate = model_df["Churn"].mean()
print(f"\nOverall churn rate: {churn_rate:.2%}")

for col in ["Geography", "Gender", "IsActiveMember", "NumOfProducts"]:
    summary = (
        model_df.groupby(col)["Churn"]
        .agg(customers="size", churn_rate="mean")
        .sort_values("churn_rate", ascending=False)
    )
    summary["churn_rate"] = (summary["churn_rate"] * 100).round(2)
    print(f"\nChurn by {col}:")
    print(summary)

# Age bands make the analysis easier for business stakeholders.
model_df["AgeBand"] = pd.cut(
    model_df["Age"],
    bins=[17, 29, 45, 60, 100],
    labels=["Under 30", "30-45", "46-60", "60+"]
)
age_summary = model_df.groupby("AgeBand", observed=False)["Churn"].agg(
    customers="size", churn_rate="mean"
)
age_summary["churn_rate"] = (age_summary["churn_rate"] * 100).round(2)
print("\nChurn by age band:")
print(age_summary)

# 4. VISUALIZATIONS
Path("images").mkdir(exist_ok=True)

geo = model_df.groupby("Geography")["Churn"].mean().mul(100).sort_values()
ax = geo.plot(kind="bar", title="Customer Churn Rate by Geography")
ax.set_ylabel("Churn rate (%)")
ax.set_xlabel("")
plt.tight_layout()
plt.savefig("images/churn_by_geography.png", dpi=160)
plt.show()

activity = model_df.groupby("IsActiveMember")["Churn"].mean().mul(100)
activity.index = ["Inactive", "Active"]
ax = activity.plot(kind="bar", title="Churn Rate by Customer Activity")
ax.set_ylabel("Churn rate (%)")
ax.set_xlabel("")
plt.tight_layout()
plt.savefig("images/churn_by_activity.png", dpi=160)
plt.show()

# 5. SQL ANALYSIS
conn = sqlite3.connect(":memory:")
model_df.drop(columns=["AgeBand"]).to_sql("customers", conn, index=False, if_exists="replace")

sql = """
SELECT
    Geography,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(Churn), 2) AS churn_rate_pct,
    ROUND(AVG(Balance), 2) AS avg_balance
FROM customers
GROUP BY Geography
ORDER BY churn_rate_pct DESC;
"""
print("\nSQL geography analysis:")
print(pd.read_sql_query(sql, conn))

# 6. FEATURE ENGINEERING + MODELLING
# AgeBand was created for stakeholder analysis; raw Age is retained for modelling.
X = model_df.drop(columns=["Churn", "AgeBand"])
y = model_df["Churn"]

categorical = ["Geography", "Gender"]
numeric = [c for c in X.columns if c not in categorical]

preprocessor = ColumnTransformer([
    ("numeric", StandardScaler(), numeric),
    ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical)
])

# Logistic regression is used as an interpretable baseline model.
pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

pipeline.fit(X_train, y_train)
pred = pipeline.predict(X_test)
prob = pipeline.predict_proba(X_test)[:, 1]

print("\n--- MODEL EVALUATION ---")
print(classification_report(y_test, pred, digits=3))
print("ROC-AUC:", round(roc_auc_score(y_test, prob), 3))

ConfusionMatrixDisplay.from_predictions(y_test, pred)
plt.title("Logistic Regression Confusion Matrix")
plt.tight_layout()
plt.savefig("images/confusion_matrix.png", dpi=160)
plt.show()

RocCurveDisplay.from_predictions(y_test, prob)
plt.title("ROC Curve — Customer Churn Model")
plt.tight_layout()
plt.savefig("images/roc_curve.png", dpi=160)
plt.show()

# 7. INTERPRETABILITY
feature_names = pipeline.named_steps["preprocess"].get_feature_names_out()
coefficients = pipeline.named_steps["model"].coef_[0]
importance = (
    pd.DataFrame({"feature": feature_names, "coefficient": coefficients})
    .assign(abs_coefficient=lambda x: x["coefficient"].abs())
    .sort_values("abs_coefficient", ascending=False)
)

print("\nLargest model coefficients:")
print(importance.head(12)[["feature", "coefficient"]].to_string(index=False))

# 8. BUSINESS OUTPUT
risk_output = X_test.copy()
risk_output["actual_churn"] = y_test.values
risk_output["predicted_churn_probability"] = prob
risk_output = risk_output.sort_values("predicted_churn_probability", ascending=False)
risk_output.to_csv("high_risk_customer_sample.csv", index=False)

print("\nAnalysis complete.")
print("Use segment findings and model probabilities to prioritize further investigation")
print("and targeted retention analysis rather than treating every customer identically.")
