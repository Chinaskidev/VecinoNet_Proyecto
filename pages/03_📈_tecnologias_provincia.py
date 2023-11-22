# Selecciono mis librerias
import streamlit as st
import pandas as pd
import plotly.express as px

# Leo mis datos
df3 = pd.read_csv('./datos_EDA/internet_accestecnologia_EDA.csv') # Leyendo mi tercer Datafram

# Uso 'markdown' y HTML para el titulo
st.markdown("<h1 style='text-align: center; color: #b6bbb5'>Tecnologías por Provincia</h1>", unsafe_allow_html=True)

# Hago un sidebar utilizando un selectbox para las Provincias
selected_province = st.selectbox('Selecciona una provincia', df3['Provincia'].unique())

# Filtrar el DataFrame según la provincia seleccionada
df_filtered = df3[df3['Provincia'] == selected_province]

# Gráfico interactivo
fig = px.bar(df_filtered.melt(id_vars='Provincia', value_vars=['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']), 
             x='variable', y='value', color='variable', 
             labels={'variable':'Tecnología', 'value':'Número de conexiones'},
             title=f'Distribución de Tecnología en {selected_province}')

fig.update_layout(showlegend=False)

st.plotly_chart(fig)

# Descripción Técnica del Gráfico y le hago un boton interactivo
if st.button('Mas Informacion'):
    st.write(
    "Este gráfico proporciona una visión detallada de la infraestructura de conexión a Internet en diversas provincias. "
    "Al utilizar el menú desplegable para seleccionar una provincia específica, se presenta la distribución "
    "de conexiones por tecnología en esa área geográfica."
)
if st.button('Ocultar'):
    st.empty()
