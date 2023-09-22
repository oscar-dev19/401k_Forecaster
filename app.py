import streamlit as st
import numpy as np
import plotly.express as px

# Function to calculate 401(k) investment forecast
def calculate_401k_forecast(current_age, retirement_age, initial_contribution, contribution_percentage,
                            annual_salary, annual_salary_increase, current_401k_contribution, annual_rate_of_return):
    years_to_retirement = retirement_age - current_age
    investment_forecast = [initial_contribution]
    total_contributions = [initial_contribution]

    for year in range(1, years_to_retirement + 1):
        annual_contribution = (annual_salary * contribution_percentage / 100) + current_401k_contribution
        total_contributions.append(total_contributions[-1] + annual_contribution)
        investment_forecast.append(
            investment_forecast[-1] * (1 + annual_rate_of_return / 100) + annual_contribution
        )

    return list(range(current_age, retirement_age + 1)), investment_forecast

st.title("401(k) Investment Forecast")

# Input fields for 401(k)
current_age = st.number_input("Current Age:", min_value=0, value=30)
retirement_age = st.number_input("Retirement Age:", min_value=current_age + 1, value=65)
initial_contribution = st.number_input("Initial 401(k) Contribution ($):", min_value=0, value=10000)
contribution_percentage = st.number_input("Contribution Percentage (% of Salary):", min_value=0, value=10)
annual_salary = st.number_input("Annual Salary ($):", min_value=0, value=60000)
annual_salary_increase = st.number_input("Annual Salary Increase (%):", min_value=0, value=3)
current_401k_contribution = st.number_input("Current 401(k) Contribution ($):", min_value=0, value=5000)
annual_rate_of_return = st.number_input("Annual Rate of Return (%):", min_value=0, value=7)

# Calculate 401(k) investment forecast using the function
x_values, y_values = calculate_401k_forecast(current_age, retirement_age, initial_contribution,
                                              contribution_percentage, annual_salary, annual_salary_increase,
                                              current_401k_contribution, annual_rate_of_return)

# Create a line chart
fig = px.line(x=x_values, y=y_values, labels={"x": "Age", "y": "Balance ($)"})
fig.update_layout(title="401(k) Investment Forecast")

# Display the chart
st.plotly_chart(fig)
