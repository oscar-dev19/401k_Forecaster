
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

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
    html.Label("Employer Match (%):"),  # New input for employer match
    dcc.Input(id="employer-match-input", type="number", value=3),  # Default to 3% match
    # Output graph to display results
    dcc.Graph(id="investment-forecast-graph"),
])

def calculate_investment_forecast(age, initial_contribution, contribution_increase, employer_match):
    # Validate inputs and provide default values if necessary
    age = max(age, 0) if age is not None else 30
    initial_contribution = max(initial_contribution, 0) if initial_contribution is not None else 10000
    contribution_increase = max(contribution_increase, 0) if contribution_increase is not None else 3
    employer_match = max(employer_match, 0) if employer_match is not None else 3

    # Calculate 401(k) investment forecast with employer match
    years_to_retirement = 65 - age
    investment_forecast = [initial_contribution]

    for year in range(1, years_to_retirement + 1):
        employer_contribution = investment_forecast[-1] * (employer_match / 100)
        investment_forecast.append(
            investment_forecast[-1] * (1 + contribution_increase / 100) + employer_contribution
        )

    x_values = list(range(age, 66))
    y_values = investment_forecast

    return x_values, y_values

@app.callback(
    Output("investment-forecast-graph", "figure"),
    [
        Input("age-input", "value"),
        Input("initial-contribution-input", "value"),
        Input("contribution-increase-input", "value"),
        Input("employer-match-input", "value"),  # New input for employer match
    ],
)
def update_investment_forecast_graph(age, initial_contribution, contribution_increase, employer_match):
    x_values, y_values = calculate_investment_forecast(age, initial_contribution, contribution_increase, employer_match)

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
