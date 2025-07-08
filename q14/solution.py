import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=6, freq='ME'),
    'sales': [100, 150, 130, 170, 160, 180]
})

df_sales.set_index('date')['sales'].plot(kind='bar', title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
