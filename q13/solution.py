import plotly.express as px
df_scatter = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50),
    'category': np.random.choice(['A', 'B'], size=50)
})

fig = px.scatter(df_scatter, x='x', y='y', color='category', title="Interactive Scatter Plot")
fig.show()
