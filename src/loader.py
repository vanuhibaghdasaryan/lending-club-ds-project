import pandas as pd

def load_data(path="data/loan.csv"):
    print("Loading data...")
    return pd.read_csv(path, low_memory=False)
