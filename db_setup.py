import os
import sqlite3

if os.path.exists("sellers.db"):
    os.remove("sellers.db")

conn = sqlite3.connect("sellers.db")
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
print("Database ready")
