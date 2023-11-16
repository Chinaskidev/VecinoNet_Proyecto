import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos (asegúrate de tener tu DataFrame df4 cargado)
df4 = pd.read_csv('./datos_EDA/internet_ingresos_EDA.csv')

# Gráfico de Área interactivo con Plotly Express
fig = px.area(df4, x='Año', y='Ingresos (miles de pesos)', color='Trimestre',
              title='Ingresos por Año y Trimestre', labels={'Ingresos (miles de pesos)': 'Ingresos'})

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)