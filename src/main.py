from pathlib import Path
import sqlite3

try:
    #Set database path properly

    BASE_DIR=Path(__file__).resolve().parent.parent
    db_path=BASE_DIR/"data"/"bookstore.db"
    conn =sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("PRAGMA foreign_keys =ON;")
    print("✓ Books table created successfully")

    # Create Books Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price REAL NOT NULL,
        stock_quantity INTEGER DEFAULT 0 
    );             
    """)
    print("✓ Books table created successfully")
    # Create Customers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        city TEXT,
        join_date TEXT          
    );
    """)
    print("✓ Customers table created successfully")
    # Create Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        book_id INTEGER,
        quantity INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        total_amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (book_id) REFERENCES books(book_id)
    );
    """)
    print("✓ Orders table created successfully")

    conn.commit()

    # Display Schema
    for table in ["books", "customers", "orders"]:
        print(f"\nSchema for {table}:")
        schema = cursor.execute(f"PRAGMA table_info({table});").fetchall()
        for row in schema:
            print(row)

except Exception as e:
    print("Error:", e)

finally:
    conn.close()