# Пікові години (за кількістю замовлень):
# hour
# 12    2520
# 13    2455
# 18    2399

import pandas as pd

# Завантаження даних про замовлення
orders = pd.read_csv('orders.csv')

# Виділення години замовлення
orders['hour'] = pd.to_datetime(orders['time']).dt.hour

# Підрахунок кількості замовлень за кожну годину
hourly_order_counts = orders['hour'].value_counts()

# Знаходження пікових годин (наприклад, топ-3 години за кількістю замовлень)
peak_hours = hourly_order_counts.head(3)

print("Пікові години (за кількістю замовлень):")
print(peak_hours)
