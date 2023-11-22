import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
df5 = pd.read_csv('./datos_EDA/Internet_Penetracion_EDA.csv')

# Limpiar datos
df5 = df5.drop(['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6'], axis=1)
df5['Accesos por cada 100 hogares'] = df5['Accesos por cada 100 hogares'].str.replace(',', '') 
df5['Accesos por cada 100 hogares'] = pd.to_numeric(df5['Accesos por cada 100 hogares'], errors='coerce')

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1 style='text-align: center; color: #b6bbb5'>KPI del 2% de Internet por Trimestre a 100 hogares</h1>", unsafe_allow_html=True)


# Entrada del usuario para el KPI
kpi = st.number_input('Introduce el valor del KPI', value=2.0)

# Cálculo del nuevo acceso
df5['NUEVOACCESO'] = ((kpi/100)*df5['Accesos por cada 100 hogares'])+df5['Accesos por cada 100 hogares']

# Selección de la provincia
provincia = st.selectbox('Selecciona una provincia', df5['Provincia'].unique())

# Filtrado de los datos por la provincia seleccionada
df5 = df5[df5['Provincia'] == provincia]


# Tarjeta de métricas para el KPI
st.metric(label="KPI", value=kpi)

# Tarjeta de métricas para el nuevo acceso
st.metric(label="Nuevo Acceso", value=df5['NUEVOACCESO'].sum())

# Ordena los datos por 'Trimestre' de forma ascendente
df5 = df5.sort_values(by=['Año', 'Trimestre'], ascending=[False, False])


# Crea el gráfico con Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=df5, x='Trimestre', y='NUEVOACCESO')

# Añade un título y etiquetas a los ejes
plt.title(' KPI Nuevo Acceso a Internet por Trimestre')
plt.xlabel('Trimestre')
plt.ylabel('NUEVOACCESO')

# Muestra el gráfico
st.pyplot(plt.gcf())

# Visualización de datos
st.dataframe(df5)
if st.button('Más Informacion'):
    st.markdown('El KPI (Indicador Clave de Rendimiento) en esta aplicación representa un objetivo de aumento en el acceso a Internet. Es un porcentaje que se aplica a los datos existentes de acceso a Internet por cada 100 hogares en una provincia específica.')
    st.markdown('Este KPI se utiliza para calcular un nuevo valor de acceso, que es el acceso original más un porcentaje del acceso original.')
    st.markdown('Por ejemplo, si el KPI es del 2%, esto significa que estamos buscando aumentar el acceso a Internet en un 2%. Por lo tanto, el nuevo acceso se calcula sumando el 2% del acceso original al acceso original.')
if st.button('Ocultar'):
    st.empty()