# 59 (59.6)

import sqlite3

conn = sqlite3.connect('pizza_database.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT AVG(daily_orders) AS average_customers_per_day
    FROM (
        SELECT COUNT(*) AS daily_orders
        FROM orders
        GROUP BY date
    ) AS subquery;
''')

result = cursor.fetchone()[0]
print("Середньо клієнтів на день:", result)

conn.close()
