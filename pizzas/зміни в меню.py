# Менш популярні піци (за кількістю замовлень):
# ital_cpcllo_s    1
# hawaiian_l       1
# veggie_veg_l     1
# є сенс прибрати ці три піци

import pandas as pd
# Завантаження даних про піци
pizzas = pd.read_csv('pizzas.csv')

# Підрахунок кількості замовлень для кожної піци
pizza_order_counts = pizzas['pizza_id'].value_counts()

# Знаходження менш популярних піц (наприклад, топ-3 піци з меншою кількістю замовлень)
less_popular_pizzas = pizza_order_counts.tail(3)

print("Менш популярні піци (за кількістю замовлень):")
print(less_popular_pizzas)
