import sqlite3
import pandas as pd

def load_data():
    conn = sqlite3.connect("sellers.db")
    df = pd.read_sql("SELECT * FROM sellers", conn)
    conn.close()
    return df

def analyze(df):
    print(df.head())
    print(df.info())
    print(df.describe())

    print("Average Rating:", df["ratings"].mean())

    top = df.loc[df["ratings"].idxmax()]
    print("\nTop Seller:\n", top)

    sorted_df = df.sort_values(by="ratings", ascending=False)
    print(sorted_df[["seller_name","ratings","orders","revenue"]])

    print("\nCorrelation:\n", df[["ratings","orders","revenue"]].corr())
