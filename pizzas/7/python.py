# Середня кількість піц в замовленні восени: 1.0201677823913227
# хоча виглядає не дуже правдоподібно

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT AVG(quantity) AS average_pizzas_per_order
    FROM orders
    JOIN order_details ON orders.order_id = order_details.order_id
    WHERE orders.date BETWEEN '2015-09-01' AND '2015-11-30';
''')

result = cursor.fetchone()[0]
print("Середня кількість піц в замовленні восени:", result)

conn.close()
