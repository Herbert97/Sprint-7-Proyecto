import pandas as pd
import plotly.express as px
import streamlit as st
import os

# obtener la ruta del archivo en la misma carpeta que app.py
file_path = os.path.join(os.path.dirname(__file__), "vehicles_us.csv")

car_data = pd.read_csv(file_path)  # leer los datos
###
#car_data = pd.read_csv(r"C:\Users\falco\OneDrive\Documentos\SPRINT7\vehicles_us.csv") # leer los datos
# ✅ Encabezado de la app
st.header("Análisis de Datos de Vehículos")

hist_button = st.button('Construir histograma') # crear un botón
   
#if hist_button: # al hacer clic en el botón
    # escribir un mensaje
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
#    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
#    st.plotly_chart(fig, use_container_width=True)

"""if hist_button:
    st.write("Creación de un histograma para la columna odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión (odometer vs price)")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)"""

    # Casilla para histograma
build_histogram = st.checkbox("Mostrar histograma de odometer")
if build_histogram:
    st.write("Construcción de histograma para la columna odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para dispersión
build_scatter = st.checkbox("Mostrar gráfico de dispersión (odometer vs price)")
if build_scatter:
    st.write("Construcción de diagrama de dispersión (odometer vs price)")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)