# Lectura de mis Datos.
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df5 = pd.read_csv('./datos_EDA/Internet_Penetracion_EDA.csv')


# Limpiar datos
df5 = df5.drop(['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6'], axis=1)
df5['Accesos por cada 100 hogares'] = df5['Accesos por cada 100 hogares'].str.replace(',', '') 
df5['Accesos por cada 100 hogares'] = pd.to_numeric(df5['Accesos por cada 100 hogares'], errors='coerce')

# Crear columna NUEVOACCESO
kpi = 2
df5['NUEVOACCESO'] = ((kpi/100) * df5['Accesos por cada 100 hogares']) + df5['Accesos por cada 100 hogares'] 

# Este codigo se utiliza para desactivar los mensaje de 'Advertencia'
st.set_option('deprecation.showPyplotGlobalUse', False)

# Estilo para el gráfico.
sns.set(style="darkgrid")

# Configuración de la aplicación Streamlit
st.markdown("<h4 style='text-align: center;'>KPI Aumento del 2% de Internet por Trimestre</h4>", unsafe_allow_html=True)
# Widget para seleccionar trimestres
trimestres_seleccionados = st.multiselect('Seleccionar Trimestre(s)', df5['Trimestre'].unique(), df5['Trimestre'].unique())

# Filtrar el DataFrame según los trimestres seleccionados
df_filtered = df5[df5['Trimestre'].isin(trimestres_seleccionados)] if trimestres_seleccionados else df5

# Gráfico interactivo
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='Trimestre', y='NUEVOACCESO', data=df_filtered, marker='o', color='darkblue', linewidth=2, ax=ax)
ax.set(xlabel='Trimestre', ylabel='KPI (%)', title='KPI de Aumento en Acceso a Internet de el 2% por Trimestre')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right')  # Rotar las etiquetas del eje x para mayor legibilidad
st.pyplot(fig)