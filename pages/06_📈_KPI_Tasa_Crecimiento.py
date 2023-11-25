import streamlit as st
import pandas as pd
import plotly.express as px


# Carga de datos
df5 = pd.read_csv('./datos_EDA/Internet_Penetracion_EDA.csv')

# Limpiar datos
df5 = df5.drop(['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6'], axis=1)
df5['Accesos por cada 100 hogares'] = df5['Accesos por cada 100 hogares'].str.replace(',', '') 
df5['Accesos por cada 100 hogares'] = pd.to_numeric(df5['Accesos por cada 100 hogares'], errors='coerce')


st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1 style='text-align: center'> KPI del 2% de Tasa de Crecimiento de Internet en Provincias</h1><hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)


# Entrada del usuario para el KPI
kpi = st.number_input('Introduce el valor del KPI', value=2.0)

# Cálculo del nuevo acceso
df5['NUEVOACCESO'] = ((kpi/100)*df5['Accesos por cada 100 hogares'])+df5['Accesos por cada 100 hogares']

# Cálculo de la tasa de crecimiento
df5['TASA_CRECIMIENTO'] = df5['NUEVOACCESO'].pct_change()

# Selección de la provincia
provincia = st.selectbox('Selecciona una provincia', df5['Provincia'].unique())

# Filtrado de los datos por la provincia seleccionada
df5 = df5[df5['Provincia'] == provincia]

# Tarjeta de métricas para el KPI
st.metric(label="KPI", value=kpi)

# Tarjeta de métricas para la tasa de crecimiento
st.metric(label="Tasa de Crecimiento", value=df5['TASA_CRECIMIENTO'].mean())

# Calcula la media móvil con una ventana de 3
df5['NUEVOACCESO'] = df5['NUEVOACCESO'].rolling(window=3).mean()

# Crea el gráfico de pastel con Plotly
fig = px.pie(df5, values='NUEVOACCESO', names='Año', title='Nuevo Acceso a Internet a lo largo de los Años')

# Actualiza los trazos del gráfico
fig.update_traces(marker=dict(colors=px.colors.sequential.Plasma))

st.plotly_chart(fig)

# Gráfico interactivo de la tasa de crecimiento con Plotly
fig2 = px.bar(df5, y='TASA_CRECIMIENTO', x='Año', color='Año', title='Tasa de Crecimiento del Acceso a Internet')

st.plotly_chart(fig2)

# Visualización de datos
st.dataframe(df5)

if st.button('Mas Informacion'):
    st.markdown('La Tasa de Crecimiento del Acceso a Internet es un KPI (Indicador Clave de Rendimiento) que representa el cambio porcentual en el acceso a Internet de un período a otro.')
    st.markdown('Este KPI se calcula utilizando la fórmula de crecimiento porcentual, que compara el nuevo acceso a Internet con el acceso anterior. Por ejemplo, si el acceso a Internet en un trimestre es de 100 hogares y en el siguiente trimestre aumenta a 102 hogares, la tasa de crecimiento sería del 2%.')
    st.markdown('Esto significa que el acceso a Internet ha crecido un 2% de un trimestre a otro.')
    st.markdown('Este KPI es útil para medir el progreso en el aumento del acceso a Internet. Un aumento en esta tasa de crecimiento indica un mayor acceso a Internet, mientras que una disminución podría indicar problemas que necesitan ser abordados.')
if st.button('Ocultar'):
    st.empty()
