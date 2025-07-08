
import pandas as pd
df_dates = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2024-03-15', '2022-11-20'])
})

df_dates['year'] = df_dates['date'].dt.year
df_dates['month'] = df_dates['date'].dt.month
print(df_dates)
