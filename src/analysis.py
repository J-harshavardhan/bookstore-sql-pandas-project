from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "data" / "bookstore.db"

conn = sqlite3.connect(db_path)

# Load tables
books_df = pd.read_sql("SELECT * FROM books", conn)
customers_df = pd.read_sql("SELECT * FROM customers", conn)
orders_df = pd.read_sql("SELECT * FROM orders", conn)

print("Books DF:\n", books_df.head(3))
print("\nCustomers DF:\n", customers_df.head(3))
print("\nOrders DF:\n", orders_df.head(3))

# Merge
report = (
    orders_df
    .merge(customers_df, on="customer_id")
    .merge(books_df, on="book_id")
)

report = report[[
    "order_id", "name", "city",
    "title", "quantity", "total_amount"
]]

print("\nComprehensive Report:\n", report)

# Analysis
print("\nAverage Order Value:", orders_df["total_amount"].mean())

print("\nOrders by City:")
print(report.groupby("city")["order_id"].count())

print("\nMost Popular Book:")
print(report.groupby("title")["quantity"].sum().sort_values(ascending=False).head(1))

# Pandas → SQL
discounts_df = pd.DataFrame({
    'book_id': [1,2,3,4,5],
    'discount_percent': [10,15,5,20,12]
})

discounts_df.to_sql("discounts", conn, if_exists="replace", index=False)

print("\nDiscounts Table:")
print(pd.read_sql("SELECT * FROM discounts", conn))

print("\nBooks with Discounted Prices:")
print(pd.read_sql("""
    SELECT b.title,
           b.price AS original_price,
           d.discount_percent,
           ROUND(b.price * (1 - d.discount_percent/100.0), 2) AS discounted_price
    FROM books b
    JOIN discounts d
    ON b.book_id = d.book_id;
""", conn))

conn.close()