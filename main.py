import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")

option_x = st.selectbox("Select the data for X-axis",
                        ('Happiness', 'Generosity', 'GDP'))

option_y = st.selectbox("Select the data for Y-axis",
                        ('Happiness', 'Generosity', 'GDP'))

st.subheader(f"{option_x} and {option_y}")

match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

figure = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure)
