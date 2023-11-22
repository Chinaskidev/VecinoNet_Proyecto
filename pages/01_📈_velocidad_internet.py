import streamlit as st
import pandas as pd
import plotly.express as px

# Lectura de mis datos para poder graficar en Streamlit
df1= pd.read_csv('./datos_EDA/historico_veloci_internetmediabaja_EDA.csv')

# Encabezado de la aplicación
st.markdown("<h1 style='text-align: center; color: #b6bbb5'>Velocidad Promedio de Descarga de Internet</h1>", unsafe_allow_html=True)

# Agrupo los datos con la columna 'Provincia' seguido de 'Mbps Media de bajada'
datos_agrupados = df1.groupby('Provincia')['Mbps (Media de bajada)'].mean().sort_values(ascending=False)

# Creo una barra de deslizamiento para interactuar con el gráfico
provincias_seleccionadas = st.slider("Selecciona el número de provincias a mostrar", 1, len(datos_agrupados), 5)

# Se filtran las provincias según la selección del usuario
provincias_filtradas = datos_agrupados.head(provincias_seleccionadas)

# Crear el gráfico interactivo con Plotly
fig = px.bar(provincias_filtradas, y='Mbps (Media de bajada)', labels={'index': 'Provincia', 'value': 'Mbps (Media de bajada)'}, title='Velocidad de Internet en Provincias')
st.plotly_chart(fig)

# boton y descripcíon del gráfico.
if st.button('Informacion del Gráfico'):
    
    st.write('Este gráfico muestra la velocidad promedio de descarga de Internet en diferentes provincias, la información se basa en datos históricos recopilados y se presenta de manera interactiva. La visualización te permite explorar y comparar las velocidades de Internet en las provincias seleccionadas.')
if st.button('Ocultar'):
    st.empty()
