import pandas as pd
import numpy as np
import re

DEFAULT_STATUSES = ["Charged Off", "Default", "Late (31-120 days)"]
NON_DEFAULT_STATUSES = ["Fully Paid", "Current"]

def parse_emp_length(x):
    if pd.isna(x):
        return np.nan
    s = str(x).lower()
    if "<" in s:
        return 0
    if "10+" in s:
        return 10
    m = re.search(r"\d+", s)
    return int(m.group()) if m else np.nan

def clean_data(df):
    print("Cleaning data...")

    required_cols = [
        "issue_d",
        "loan_status",
        "loan_amnt",
        "int_rate",
        "grade",
        "sub_grade",
        "purpose",
        "annual_inc",
        "dti",
        "emp_length"
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df[required_cols].copy()

    # Parse date
    df["issue_d"] = pd.to_datetime(df["issue_d"], format="%b-%Y", errors="coerce")

    # Create binary target
    df["default"] = np.where(
        df["loan_status"].isin(DEFAULT_STATUSES), 1,
        np.where(df["loan_status"].isin(NON_DEFAULT_STATUSES), 0, np.nan)
    )

    # Parse employment length
    # Parse employment length
    df["emp_length"] = df["emp_length"].apply(parse_emp_length)

    # Drop rows without date or target
    df = df.dropna(subset=["issue_d", "default"])

    # Monthly helper
    df["year_month"] = df["issue_d"].dt.to_period("M").astype(str)

    return df
