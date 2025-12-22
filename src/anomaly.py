def detect_anomalies(monthly_df, threshold=2):
    print("Detecting anomalies...")
    mean = monthly_df["default_rate"].mean()
    std = monthly_df["default_rate"].std()

    monthly_df["anomaly"] = (
        (monthly_df["default_rate"] - mean).abs() > threshold * std
    )
    return monthly_df
