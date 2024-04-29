# Кількість замовлень за кожен місяць:
# month
# 1     1845
# 2     1685
# 3     1840
# 4     1799
# 5     1853
# 6     1773
# 7     1935
# 8     1841
# 9     1661
# 10    1646
# 11    1792
# 12    1680
# не бачу кореляції 

import pandas as pd
# Завантаження даних про замовлення
orders = pd.read_csv('orders.csv')

# Виділення місяця замовлення
orders['month'] = pd.to_datetime(orders['date']).dt.month

# Підрахунок кількості замовлень за кожен місяць
monthly_order_counts = orders['month'].value_counts()

# Відсортування результатів за місяцями
monthly_order_counts_sorted = monthly_order_counts.sort_index()

# Вивід кількості замовлень за кожен місяць (відсортовано)
print("Кількість замовлень за кожен місяць:")
print(monthly_order_counts_sorted)
