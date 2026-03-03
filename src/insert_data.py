from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "data" / "bookstore.db"

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    books_data = [
        ('Python Programming', 'John Smith', 599.99, 25),
        ('Data Science Handbook', 'Jane Doe', 899.50, 15),
        ('Machine Learning Basics', 'Alan Turing', 1299.00, 10),
        ('SQL Essentials', 'Edgar Codd', 499.99, 30),
        ('Web Development', 'Tim Berners', 799.00, 20)
    ]

    customers_data = [
        ('Rahul Sharma', 'rahul@email.com', 'Mumbai', '2024-01-15'),
        ('Priya Patel', 'priya@email.com', 'Delhi', '2024-01-20'),
        ('Amit Kumar', 'amit@email.com', 'Bangalore', '2024-02-01'),
        ('Sneha Reddy', 'sneha@email.com', 'Hyderabad', '2024-02-10'),
        ('Vikram Singh', 'vikram@email.com', 'Mumbai', '2024-02-15')
    ]

    orders_data = [
        (1, 1, 2, '2024-03-01', 1199.00),
        (1, 2, 1, '2024-03-02', 899.50),
        (2, 1, 1, '2024-03-03', 599.99),
        (2, 3, 1, '2024-03-05', 1299.00),
        (3, 4, 3, '2024-03-07', 1499.97),
        (4, 2, 1, '2024-03-10', 899.50),
        (5, 5, 2, '2024-03-12', 1598.00)
    ]

    cursor.executemany(
        "INSERT INTO books (title, author, price, stock_quantity) VALUES (?, ?, ?, ?);",
        books_data
    )

    cursor.executemany(
        "INSERT INTO customers (name, email, city, join_date) VALUES (?, ?, ?, ?);",
        customers_data
    )

    cursor.executemany(
        "INSERT INTO orders (customer_id, book_id, quantity, order_date, total_amount) VALUES (?, ?, ?, ?, ?);",
        orders_data
    )

    conn.commit()
    print("✓ Data inserted successfully")

    # Complex Queries

    print("\nCustomers from Mumbai:")
    for row in cursor.execute("SELECT * FROM customers WHERE city='Mumbai';"):
        print(row)

    print("\nBooks price > 800 AND stock > 10:")
    for row in cursor.execute("""
        SELECT * FROM books
        WHERE price > 800 AND stock_quantity > 10;
    """):
        print(row)

    total_orders = cursor.execute("SELECT COUNT(*) FROM orders;").fetchone()[0]
    print("\nTotal Orders:", total_orders)

    print("\nCustomer with most orders:")
    for row in cursor.execute("""
        SELECT customer_id, COUNT(*) as total
        FROM orders
        GROUP BY customer_id
        ORDER BY total DESC
        LIMIT 1;
    """):
        print(row)

    total_revenue = cursor.execute("SELECT SUM(total_amount) FROM orders;").fetchone()[0]
    print("\nTotal Revenue:", total_revenue)

except Exception as e:
    print("Error:", e)

finally:
    conn.close()