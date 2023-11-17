# Selecciono mis librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Leo mis datos
df3 = pd.read_csv('./datos_EDA/internet_accestecnologia_EDA.csv') # Leyendo mi tercer Datafram

# Uso 'markdown' y HTML para el titulo
st.markdown("<h1 style='text-align: center;'>Tecnologías por Provincia</h1>", unsafe_allow_html=True)

# Hago un sidebar utilizando un selectbox para las Provincias
selected_province = st.sidebar.selectbox('Selecciona una provincia', df3['Provincia'].unique())

# Filtrar el DataFrame según la provincia seleccionada
df_filtered = df3[df3['Provincia'] == selected_province]

# Gráfico interactivo
fig, ax = plt.subplots()

# Barra para cada tecnología
tecnologias = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']
for tecnologia in tecnologias:
    ax.bar(tecnologia, df_filtered[tecnologia].iloc[0], label=tecnologia, edgecolor='black')

ax.set_title(f'Distribución de Tecnología en {selected_province}')
ax.set_xlabel('Tecnología')
ax.set_ylabel('Número de conexiones')
ax.legend()

st.pyplot(fig)