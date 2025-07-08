import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 92, 78, 90]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_sorted = df.sort_values(by='Score', ascending=False)
print("\nDataFrame Sorted by Score (Descending):")
print(df_sorted)
