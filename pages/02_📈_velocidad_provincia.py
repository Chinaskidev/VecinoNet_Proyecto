# Cargo las librerias que utilizare para este gráfico.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Cargo mi Dataframe 
df2 = pd.read_csv('./datos_EDA/internetfijo_velocidadbaja_provincia_EDA.csv')

# Agrego un encabezado con 'markdown' y usando HTML
st.markdown("<h1 style='text-align: center;'>Velocidades por Provincia</h1>", unsafe_allow_html=True)

# En esta parte selecciono la velocidad a visualizar en el gráfico.
velocidad_seleccionada = st.selectbox('Selecciona la velocidad:', ['0,5 Mbps', '3 Mbps', '10 Mbps'])

# Se filtran datos según la velocidad seleccionada
df_filtrado = df2[['Provincia', velocidad_seleccionada]]

# Asigno colores según la velocidad
colores = {
    '0,5 Mbps': '#03045e',
    '3 Mbps': '#0077b6',
    '10 Mbps': '#00b4d8'
}

# Crear el gráfico de barras con colores específicos
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(df_filtrado['Provincia'], df_filtrado[velocidad_seleccionada], color=colores[velocidad_seleccionada], edgecolor='black', linewidth=1.2)

# Grafico y personalizo
ax.set_title(f'Gráfico de Barras de {velocidad_seleccionada} por Provincia')
ax.set_xlabel('Provincia')
ax.set_ylabel('Velocidad')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotar las etiquetas del eje x para mayor legibilidad
plt.xticks(rotation=45, ha='right')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)