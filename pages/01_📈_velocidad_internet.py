import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns 

df1= pd.read_csv('.\datos_EDA\historico_veloci_internetmediabaja_EDA.csv')

# Encabezado de la aplicación
st.markdown("<h1 style='text-align: center;'>Velocidad de Internet en Provincias</h1>", unsafe_allow_html=True)


# Supongamos que df1 es tu DataFrame
datos_agrupados = df1.groupby('Provincia')['Mbps (Media de bajada)'].mean().sort_values(ascending=False)

# Crear la barra de deslizamiento para interactuar con el gráfico
provincias_seleccionadas = st.slider("Selecciona el número de provincias a mostrar", 1, len(datos_agrupados), 5)


# Filtrar las provincias según la selección del usuario
provincias_filtradas = datos_agrupados.head(provincias_seleccionadas)

# Crear el gráfico interactivo con Streamlit
st.bar_chart(provincias_filtradas, use_container_width=True)


