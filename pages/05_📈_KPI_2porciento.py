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

st.set_option('deprecation.showPyplotGlobalUse', False)

# Streamlit app
def main():
    st.title('KPI del 2%')

    # Sidebar con filtro de trimestres
    selected_quarters = st.sidebar.slider('Selecciona Trimestres', min(df5['Trimestre']), max(df5['Trimestre']),
                                          (min(df5['Trimestre']), max(df5['Trimestre'])))

    # Filtrar el DataFrame
    filtered_df = df5[df5['Trimestre'].between(*selected_quarters)]
    
    # Selector de columna Y dinámico
    y_column = st.sidebar.selectbox('Selecciona la columna Y', ['NUEVOACCESO', 'Año', 'Provincia'])

    # Estilo de Seaborn
    sns.set(style="darkgrid")

    # Configurar el gráfico de líneas
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Trimestre', y=y_column, data=filtered_df, marker='o', color='darkblue', linewidth=2)
    plt.xlabel('Trimestre')
    plt.ylabel(y_column)
    plt.title('Acceso a Internet por 100 hogares')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot()

    # Mostrar el DataFrame filtrado
    st.write('Datos Filtrados:', filtered_df)

if __name__ == '__main__':
    main()