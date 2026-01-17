import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df = df.sort_values("Order Date")
    return df
