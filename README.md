# 📚 Bookstore Database Management System

## 👤 Name
J-Harsha Vardhan

## 📌 Project Overview
This project demonstrates the design and implementation of a relational SQLite database for an online bookstore. It integrates SQL operations with Pandas for analytical processing.

## 🗂 Database Schema

### 1️⃣ Books
- book_id (Primary Key)
- title
- author
- price
- stock_quantity

### 2️⃣ Customers
- customer_id (Primary Key)
- name
- email (Unique)
- city
- join_date

### 3️⃣ Orders
- order_id (Primary Key)
- customer_id (Foreign Key)
- book_id (Foreign Key)
- quantity
- order_date
- total_amount

## 🔍 Key Features
- Relational schema with constraints
- Complex SQL queries (GROUP BY, JOIN, Aggregation)
- Pandas integration for analytics
- DataFrame to SQL conversion using `.to_sql()`
- Discount calculation using SQL JOIN

## 📊 Analysis Performed
- Average Order Value
- Total Revenue
- Orders by City
- Most Popular Book
- Discounted Price Calculation

## 🛠 Tech Stack
- Python
- SQLite
- Pandas
- Google Colab

## 📂 Files Included
- `Bookstore_SQL_Pandas.ipynb`
- `bookstore.db`

---

## 🎯 Learning Outcomes
- Database normalization and constraints
- SQL aggregations and joins
- PRAGMA schema inspection
- SQL ↔ Pandas integration
- Transaction handling with commit()

---

## 🚀 How to Run
1. Open notebook in Google Colab
2. Run all cells
3. Database file will be generated automatically
