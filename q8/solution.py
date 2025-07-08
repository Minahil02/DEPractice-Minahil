import pandas as pd
import numpy as np
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8]
})
df_filled = df.fillna(df.mean(numeric_only=True))
print(df_filled)
