import sqlite3
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def create_db_and_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        order_id INTEGER PRIMARY KEY,
                        date TEXT,
                        time TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS order_details (
                        order_details_id INTEGER PRIMARY KEY,
                        order_id INTEGER,
                        pizza_id INTEGER,
                        quantity INTEGER,
                        FOREIGN KEY (order_id) REFERENCES orders(order_id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pizzas (
                        pizza_id INTEGER PRIMARY KEY,
                        pizza_type_id INTEGER,
                        size TEXT,
                        price REAL,
                        FOREIGN KEY (pizza_type_id) REFERENCES pizza_types(pizza_type_id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pizza_types (
                        pizza_type_id INTEGER PRIMARY KEY,
                        name TEXT,
                        category TEXT,
                        ingredients TEXT
                    )''')

    conn.commit()
    conn.close()

def insert_data_into_db():
    conn = sqlite3.connect('database.db')

    orders_data = load_data('orders.csv')
    orders_data.to_sql('orders', conn, if_exists='append', index=False)

    order_details_data = load_data('order_details.csv')
    order_details_data.to_sql('order_details', conn, if_exists='append', index=False)

    pizzas_data = load_data('pizzas.csv')
    pizzas_data.to_sql('pizzas', conn, if_exists='append', index=False)

    pizza_types_data = load_data('pizza_types.csv')
    pizza_types_data.to_sql('pizza_types', conn, if_exists='append', index=False)

    conn.close()

# Створення бази даних та таблиць
create_db_and_tables()

# Завантаження даних з файлів в базу даних
insert_data_into_db()
