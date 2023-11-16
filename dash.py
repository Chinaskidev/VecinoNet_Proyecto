# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Contenido de la aplicación
import streamlit as st

# Título centrado
st.markdown("<h1 style='text-align: center;'>VecinoNet(Redes para Todos) </h1>", unsafe_allow_html=True)

# Contenido centrado
st.markdown("<p style='text-align: center;'>Uniendo Vecinos, Fortaleciendo Comunidades.</p>", unsafe_allow_html=True)


# Cargar una imagen desde una carpeta local (reemplaza 'nombre_de_tu_imagen.jpg' con el nombre de tu imagen)
imagen_path = "./images/vecinonet.png"  # Reemplaza con la ruta de tu imagen
st.image(imagen_path, width=800)

# Sidebar
st.sidebar.markdown('Análisis visual a través de gráficos')






#st.set_option('deprecation.showPyplotGlobalUse', False)

# Ejecutar la aplicación
#if __name__ == "__main__":
    #st.run_app()
