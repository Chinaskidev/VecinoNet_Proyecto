# Cargar de las librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Leyendo mis datos
df1_1 = pd.read_csv('./datos_EDA/interbajada_localprovincia_EDA.csv') 

# Definición de un KPI (Key Performance Indicator) como 2
kpi = 2
# Cálculo de un nuevo valor llamado 'NUEVOACCESO' basado en el KPI y la columna existente 'Accesos por cada 100 hogares'
# La fórmula es: (KPI/100) * Accesos por cada 100 hogares + Accesos por cada 100 hogares
df1_1['NUEVOACCESO'] = ((kpi/100)*df1_1['Mbps (Media de bajada)'])+df1_1['Mbps (Media de bajada)'] 

#df1_1.dropna(inplace=True)

# Configuración de la aplicación Streamlit
st.markdown("<h4 style='text-align: center;'>KPI del 2% Internet por Provincia</h4>", unsafe_allow_html=True)
# Sidebar para widgets
st.sidebar.title('Configuración del Gráfico de Líneas')

# Widget para seleccionar provincias
provincias_seleccionadas = st.sidebar.multiselect('Seleccionar Provincia(s)', df1_1['Provincia'].unique(),
                                                  df1_1['Provincia'].unique())

# Filtrar el DataFrame según las provincias seleccionadas
df_filtered = df1_1[df1_1['Provincia'].isin(provincias_seleccionadas)] if provincias_seleccionadas else df1_1

# Configurar el estilo de Seaborn
sns.set(style="darkgrid")

# Gráfico de líneas con Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x='Provincia', y='NUEVOACCESO', data=df_filtered, marker='o', color='darkblue', linewidth=2)
plt.xlabel('Provincia')
plt.ylabel('KPI (%)')
plt.title('KPI de Aumento de velocidad al 2% a Internet por Provincia')
plt.xticks(rotation=30, ha='right')  # Roto las etiquetas del eje x para mayor legibilidad
plt.tight_layout()  # Ajusto el diseño para evitar cortar las etiquetas

# Mostrar el gráfico en la sección principal de Streamlit
st.pyplot(plt)