import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=6, freq='ME'),  # 'ME' = Month-End
    'sales': [100, 150, 130, 170, 160, 180]
})

plt.plot(df_sales['date'], df_sales['sales'], marker='o')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
