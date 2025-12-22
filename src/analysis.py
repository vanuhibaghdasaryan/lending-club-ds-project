import pandas as pd
def monthly_aggregation(df):
    print("Creating monthly aggregations...")

    monthly = (
        df
        .groupby(df["issue_d"].dt.to_period("M"))
        .agg(
            loan_count=("loan_amnt", "count"),
            avg_loan=("loan_amnt", "mean"),
            default_rate=("default", "mean")
        )
        .reset_index()
        .rename(columns={"issue_d": "year_month"})
    )

    # Convert Period to timestamp for plotting
    monthly["year_month"] = monthly["year_month"].dt.to_timestamp()

    return monthly


def grade_purpose_aggregation(df):
    print("Aggregating by grade and purpose...")
    return (
        df.groupby(["grade", "purpose"])
        .agg(
            loan_count=("loan_amnt", "count"),
            default_rate=("default", "mean")
        )
        .reset_index()
    )


