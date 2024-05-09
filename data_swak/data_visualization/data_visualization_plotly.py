import pandas as pd
import plotly.express as px

df = pd.read_csv('../../data_repo/sample-data.csv')

fig = px.scatter(df, x='x_column', y='y_column', title='Scatter Plot Example')
fig.show()

fig.update_traces(marker=dict(size=10, color='red', symbol='circle'))
fig.show()

fig.update_layout(plot_bgcolor='lightgray')
fig.update_layout(xaxis_title='X Axis Label', yaxis_title='Y Axis Label', title_text='Custom Title')
fig.show()