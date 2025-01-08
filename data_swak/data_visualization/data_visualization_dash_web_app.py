import pandas as pd
import plotly.express as px
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

df = pd.read_csv('../../data_repo/sample-data.csv')

fig = px.scatter(df, x='x_column', y='y_column', title='Scatter Plot Example')
fig.update_traces(marker=dict(size=10, color='red', symbol='circle'))
fig.update_layout(plot_bgcolor='lightgray')
fig.update_layout(xaxis_title='X Axis Label', yaxis_title='Y Axis Label', title_text='Custom Title')

app1 = Dash(__name__)

app1.layout = html.Div([
    html.H1('My Data Visualization App'),
    dcc.Graph(id='my_graph', figure=fig)
])

app2 = Dash(__name__)

app2.layout = html.Div([
    html.H1('My Interactive Data Visualization App'),
    dcc.Dropdown(id='category_dropdown',
                 options=[{'label': category, 'value': category} for category in df['category'].unique()],
                 value='All Categories'),
    dcc.Graph(id='my_graph')
])


@app2.callback(
    Output('my_graph', 'figure'),
    Input('category_dropdown', 'value'))
def update_graph(selected_category):
    if selected_category == 'All Categories':
        filtered_df = df
    else:
        filtered_df = df[df['category'] == selected_category]

    fig = px.scatter(filtered_df, x='x_column', y='y_column', title='Scatter Plot Example')
    fig.update_traces(marker=dict(size=10, color='red', symbol='circle'))
    fig.update_layout(plot_bgcolor='lightgray')
    fig.update_layout(xaxis_title='X Axis Label', yaxis_title='Y Axis Label', title_text='Custom Title')

    return fig


if __name__ == '__main__':
    # Flask app
    app2.run_server(debug=True)
