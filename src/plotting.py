import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def plot_results(monthly, grade_purpose):
    os.makedirs("outputs/plots", exist_ok=True)

    # Loan volume over time
    plt.figure()
    plt.plot(monthly["year_month"], monthly["loan_count"])
    plt.title("Loan Issuance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Loans")
    plt.tight_layout()
    plt.savefig("outputs/plots/loan_volume.png")
    plt.close()

    # Default rate over time
    plt.figure()
    plt.plot(monthly["year_month"], monthly["default_rate"])
    plt.title("Default Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Default Rate")
    plt.tight_layout()
    plt.savefig("outputs/plots/default_rate.png")
    plt.close()

    # Default rate by grade
    grade_avg = grade_purpose.groupby("grade")["default_rate"].mean()
    plt.figure()
    grade_avg.plot(kind="bar")
    plt.title("Default Rate by Loan Grade")
    plt.xlabel("Grade")
    plt.ylabel("Default Rate")
    plt.tight_layout()
    plt.savefig("outputs/plots/default_by_grade.png")
    plt.close()


def plot_issuance_and_default(monthly):
    plt.figure()
    plt.plot(monthly["year_month"], monthly["loan_count"], label="Loan Count")
    plt.plot(monthly["year_month"], monthly["default_rate"], label="Default Rate")
    plt.legend()
    plt.title("Loan Issuance and Default Rate Over Time")
    plt.tight_layout()
    plt.savefig("outputs/plots/issuance_vs_default.png")
    plt.close()


def plot_default_by_purpose(df):
    purpose_rate = (
        df.groupby("purpose")["default"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8,4))
    purpose_rate.plot(kind="bar")
    plt.title("Default Rate by Loan Purpose")
    plt.ylabel("Default Rate")
    plt.tight_layout()
    plt.savefig("outputs/plots/default_by_purpose.png")
    plt.close()




def plot_grade_purpose_heatmap(df):
    pivot = df.pivot_table(
        values="default",
        index="grade",
        columns="purpose",
        aggfunc="mean"
    )

    plt.figure(figsize=(10,4))
    sns.heatmap(pivot, cmap="Reds")
    plt.title("Default Rate Heatmap: Grade vs Purpose")
    plt.tight_layout()
    plt.savefig("outputs/plots/grade_purpose_heatmap.png")
    plt.close()



def plot_loan_amount_distribution(df):
    plt.figure()
    df[df["default"] == 0]["loan_amnt"].hist(alpha=0.6, label="Non-default")
    df[df["default"] == 1]["loan_amnt"].hist(alpha=0.6, label="Default")
    plt.legend()
    plt.title("Loan Amount Distribution by Default Status")
    plt.tight_layout()
    plt.savefig("outputs/plots/loan_amount_distribution.png")
    plt.close()


def plot_default_by_income_quantile(df):
    df = df.copy()
    df["income_q"] = pd.qcut(df["annual_inc"], 5)

    rates = df.groupby("income_q")["default"].mean()

    plt.figure()
    rates.plot(kind="bar")
    plt.title("Default Rate by Income Quintile")
    plt.tight_layout()
    plt.savefig("outputs/plots/default_by_income.png")
    plt.close()
