import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos.
df4 = pd.read_csv('./datos_EDA/internet_ingresos_EDA.csv')

# Titulo del Gráfico
st.markdown("<h1 style='text-align: center; color: #b6bbb5'>Ingresos desde 2014-2022</h1>", unsafe_allow_html=True)

# Añadir un deslizador para seleccionar el rango de años
min_year, max_year = st.slider('Selecciona el rango de años', int(df4['Año'].min()), int(df4['Año'].max()), (int(df4['Año'].min()), int(df4['Año'].max())))

# Filtrar los datos por el rango de años seleccionado
df4 = df4[(df4['Año'] >= min_year) & (df4['Año'] <= max_year)]

# Añadir un selector de trimestre
selected_quarter = st.selectbox('Selecciona un trimestre', options=df4['Trimestre'].unique(), index=0)

# Filtrar los datos por el trimestre seleccionado
df4 = df4[df4['Trimestre'] == selected_quarter]

# Gráfico de Área interactivo con Plotly Express
fig = px.area(df4, x='Año', y='Ingresos (miles de pesos)', color='Trimestre',
              title='Ingresos por Año y Trimestre', labels={'Ingresos (miles de pesos)': 'Ingresos'})

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Agrego un boton interactivo y el texto
if st.button('Más Informacion'):
    st.markdown('Al observar la evolución de los ingresos en diferentes periodos, es posible identificar patrones estacionales, tendencias a largo plazo y variaciones en los ingresos trimestrales.')
    st.markdown('Esta herramienta se convierte en un recurso valioso para analizar el rendimiento financiero de los servicios de Internet, permitiendo a las partes interesadas tomar decisiones informadas basadas en datos concretos.')
    st.markdown('La capacidad de filtrar por año y trimestre ofrece una perspectiva más detallada y contextualizada, facilitando la identificación de áreas de crecimiento o declive en los ingresos. Además, la representación gráfica mediante áreas resalta claramente la contribución relativa de cada trimestre al panorama general de ingresos.')
if st.button('Ocultar'):
    st.empty()