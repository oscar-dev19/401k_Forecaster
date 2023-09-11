import dash
from dash import dcc, html
from dash.dependencies import Input, Output

#these dependencies allows github pages to render app
import dash_renderer




app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("401(k) Investment Forecast"),

    # Input fields for 401(k)
    html.Label("Age:"),
    dcc.Input(id="age-input", type="number", value=30),

    html.Label("Initial Contribution ($):"),
    dcc.Input(id="initial-contribution-input", type="number", value=10000),

    html.Label("Annual Contribution Increase (%):"),
    dcc.Input(id="contribution-increase-input", type="number", value=3),

    # Output graph to display results
    dcc.Graph(id="investment-forecast-graph"),
])

@app.callback(
    Output("investment-forecast-graph", "figure"),
    [
        Input("age-input", "value"),
        Input("initial-contribution-input", "value"),
        Input("contribution-increase-input", "value"),
    ],
)
def update_investment_forecast_graph(age, initial_contribution, contribution_increase):
    # Check for None values and provide default values
    age = age if age is not None else 30
    initial_contribution = initial_contribution if initial_contribution is not None else 10000
    contribution_increase = contribution_increase if contribution_increase is not None else 3

    # Calculate 401(k) investment forecast
    years_to_retirement = 65 - age
    investment_forecast = [initial_contribution]

    for year in range(1, years_to_retirement + 1):
        investment_forecast.append(
            investment_forecast[-1] * (1 + contribution_increase / 100)
        )

    x_values = list(range(age, 66))
    y_values = investment_forecast

    fig = {
        'data': [
            {
                'x': x_values,
                'y': y_values,
                'type': 'line',
                'mode': 'lines+markers',
                'name': '401(k) Forecast',
            },
        ],
        'layout': {
            'title': '401(k) Investment Forecast',
            'xaxis': {'title': 'Age'},
            'yaxis': {'title': 'Balance ($)'},
        }
    }

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
    app.scripts.config.serve_locally = True
    app.css.config.serve_locally = True

