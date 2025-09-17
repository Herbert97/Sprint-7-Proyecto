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
   
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)