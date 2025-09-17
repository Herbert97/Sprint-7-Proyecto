import pandas as pd
import plotly.express as px
import streamlit as st
import os

# obtener la ruta del archivo en la misma carpeta que app.py
file_path = os.path.join(os.path.dirname(__file__), "vehicles_us.csv")

car_data = pd.read_csv(file_path)  # leer los datos

st.header("Análisis de Datos de Vehículos")

# Checkbox para histograma
if st.checkbox("Construir un histograma"):
    st.write("Creación de un histograma para la columna odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para dispersión
if st.checkbox("Construir gráfico de dispersión"):
    st.write("Creación de un gráfico de dispersión (odometer vs price)")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

    