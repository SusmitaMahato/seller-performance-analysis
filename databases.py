# Reset old DB
import os

if os.path.exists("sellers.db"):
    os.remove("sellers.db")

print("Old DB cleared")

# Create DB + Table
import sqlite3

conn = sqlite3.connect("sellers.db", timeout=10)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE sellers (
    seller_id INTEGER PRIMARY KEY,
    seller_name TEXT,
    category TEXT,
    ratings REAL,
    orders INTEGER,
    revenue REAL
)
""")

conn.commit()
conn.close()

print("Table created")

# Insert data
import sqlite3

conn = sqlite3.connect("sellers.db", timeout=10)
cursor = conn.cursor()

cursor.executemany("""
INSERT INTO sellers VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, "Seller A", "Electronics", 4.5, 1200, 250000),
    (2, "Seller B", "Fashion", 3.8, 800, 120000),
    (3, "Seller C", "Electronics", 4.2, 950, 210000),
    (4, "Seller D", "Home", 2.9, 400, 60000),
    (5, "Seller E", "Fashion", 4.8, 1500, 300000)
])

conn.commit()
conn.close()

print("Data inserted")

# Load into Pandas
import sqlite3
import pandas as pd

conn = sqlite3.connect("sellers.db")
df = pd.read_sql("SELECT * FROM sellers", conn)
conn.close()

df

# Understand the data
print(df.head())
print(df.info())
print(df.describe())

# Core analysis
avg_rating = df["ratings"].mean()
print("Average Rating:", avg_rating)

top_seller = df.loc[df["ratings"].idxmax()]
print("\nTop Seller:\n", top_seller)

df_sorted = df.sort_values(by="ratings", ascending=False)
print(df_sorted[["seller_name", "ratings", "orders", "revenue"]])

print("\nCorrelation Matrix:\n", df[["ratings", "orders", "revenue"]].corr())

# Visualizations
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(y=df["ratings"])
plt.title("Ratings Distribution")
plt.show()

sns.boxplot(x="category", y="ratings", data=df)
plt.title("Category-wise Ratings")
plt.show()

sns.barplot(x="seller_name", y="ratings", data=df)
plt.title("Seller Ratings")
plt.show()

sns.barplot(x="seller_name", y="revenue", data=df)
plt.title("Seller Revenue")
plt.show()

# Mini Dashboard
plt.figure(figsize=(10,6))

plt.subplot(1,2,1)
sns.boxplot(y=df["ratings"])
plt.title("Ratings")

plt.subplot(1,2,2)
sns.barplot(x="seller_name", y="ratings", data=df)
plt.title("Seller Ratings")

plt.tight_layout()
plt.show()

