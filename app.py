import streamlit as st
import numpy as np
import plotly.express as px

st.title("401(k) Investment Forecast")

# Input fields for 401(k)
age = st.number_input("Age:", min_value=0, value=30)
initial_contribution = st.number_input("Initial Contribution (﹩):", min_value=0, value=10000)
contribution_increase = st.number_input("Annual Contribution Increase (%):", min_value=0, value=3)
employer_match = st.number_input("Employer Match (%):", min_value=0, value=3)  # New input for employer match

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

# Create a line chart
fig = px.line(x=x_values, y=y_values, labels={"x": "Age", "y": "Balance (﹩)"})
fig.update_layout(title="401(k) Investment Forecast")

# Display the chart
st.plotly_chart(fig)

