import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT SUM(pizzas.price * order_details.quantity) AS revenue
    FROM pizzas
    JOIN order_details ON pizzas.pizza_id = order_details.pizza_id
    JOIN (
        SELECT order_details.pizza_id, SUM(order_details.quantity) AS total_quantity
        FROM order_details
        JOIN orders ON order_details.order_id = orders.order_id
        WHERE strftime('%m', orders.date) = '06'
        GROUP BY order_details.pizza_id
        ORDER BY total_quantity DESC
        LIMIT 3
    ) AS popular_pizzas ON pizzas.pizza_id = popular_pizzas.pizza_id;
''')

result = cursor.fetchone()[0]
print("Загальний дохід від трьох найпопулярніших піц у червні:", result)

conn.close()
