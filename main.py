from src.loader import load_data
from src.cleaning import clean_data
from src.analysis import monthly_aggregation, grade_purpose_aggregation
from src.anomaly import detect_anomalies
from src.modeling import run_model
from src.plotting import (
    plot_results,
    plot_issuance_and_default,
    plot_default_by_purpose,
    plot_loan_amount_distribution,
    plot_default_by_income_quantile,
    plot_grade_purpose_heatmap,
    plot_default_rate_with_anomalies
)

import os

def main():
    os.makedirs("outputs/processed", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)
    os.makedirs("outputs/reports", exist_ok=True)

    # Load & clean
    df = load_data()
    df = clean_data(df)

    # Analysis
    monthly = monthly_aggregation(df)
    grade_purpose = grade_purpose_aggregation(df)
    monthly = detect_anomalies(monthly)
    plot_default_rate_with_anomalies(monthly)
    plot_grade_purpose_heatmap(df)

    # Save processed data
    monthly.to_csv("outputs/processed/monthly.csv", index=False)
    grade_purpose.to_csv("outputs/processed/grade_purpose.csv", index=False)

    # Modeling
    auc = run_model(df)
    with open("outputs/reports/model_results.txt", "w") as f:
        f.write(f"ROC-AUC: {auc:.4f}")

    # Plots
    plot_results(monthly, grade_purpose)
    plot_issuance_and_default(monthly)
    plot_default_by_purpose(df)
    plot_loan_amount_distribution(df)
    plot_default_by_income_quantile(df)
    plot_default_rate_with_anomalies(monthly)
    plot_grade_purpose_heatmap(df)

    print("ALL PLOTS CREATED SUCCESSFULLY")

if __name__ == "__main__":
    main()
