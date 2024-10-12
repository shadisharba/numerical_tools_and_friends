# https://www.statworx.com/at/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv("data/stockdata2.csv", index_col=0, parse_dates=True)
df.index = pd.to_datetime(df["csvDate"])

# Initialise the app
app = dash.Dash(__name__)

graph1 = dcc.Graph(
    id="timeseries_all",
    config={"displayModeBar": False},
    animate=True,
    figure=px.line(
        df,
        x="csvDate",
        y="csvvalue",
        color="csvstock",
    ),
)
graph2 = dcc.Graph(id="timeseries", config={"displayModeBar": False})


# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({"label": i, "value": i})
    return dict_list


drop_down = html.Div(
    className="div-for-dropdown",
    children=[
        dcc.Dropdown(
            id="stockselector", options=get_options(df["csvstock"].unique()), multi=True, value=[df["csvstock"].sort_values()[0]], style={"backgroundColor": "white"}, className="stockselector"
        )
    ],
    style={"color": "white"},
)

top_left = html.Div(className="two columns div-user-controls bg-red", children=[html.H2("Dash - STOCK PRICES"), html.P("Visualising time series with Plotly"), drop_down])

top_right = html.Div(className="ten columns div-for-charts bg-green", children=[graph1])

bottom_left = html.Div(
    className="two columns div-user-controls bg-red",
    children=[
        html.H2("Dash - STOCK PRICES"),
        html.P("""Visualising time series with Plotly - Dash"""),
    ],
)

bottom_right = html.Div(className="ten columns div-user-controls bg-red", children=[graph2])


@app.callback(Output("timeseries", "figure"), [Input("stockselector", "value")])
def update_timeseries(selected_dropdown_value):
    """Draw traces of the feature 'value' based one the currently selected stocks"""
    trace = []
    df_sub = df
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub["csvstock"] == stock].index, y=df_sub[df_sub["csvstock"] == stock]["csvvalue"], mode="lines", opacity=0.7, name=stock, textposition="bottom center"))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    figure = {
        "data": data,
        "layout": go.Layout(
            # colorway=["#5E0DAC", "#FF4F00", "#375CB1", "#FF7400", "#FFF400", "#FF0056"],
            # template="plotly_dark",
            # paper_bgcolor="rgba(0, 0, 0, 0)",
            # plot_bgcolor="rgba(0, 0, 0, 0)",
            margin={"b": 15},
            hovermode="x",
            autosize=True,
            title={"text": "Stock Prices", "font": {"color": "white"}, "x": 0.5},
            xaxis={"range": [df_sub.index.min(), df_sub.index.max()]},
        ),
    }

    return figure


# Define the app
app.layout = html.Div(children=[html.Div(className="row1", children=[top_left, top_right]), html.Div(className="row2", children=[bottom_left, bottom_right])])

if __name__ == "__main__":
    app.run_server(debug=True)
