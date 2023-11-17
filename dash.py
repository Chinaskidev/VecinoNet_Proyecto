# Importo la libreria
import streamlit as st


# Título centradonusando HTML
st.markdown("<h1 style='text-align: center;'>VecinoNet(Redes para Todos) </h1>", unsafe_allow_html=True)

# Contenido centrado
st.markdown("<p style='text-align: center;'>Uniendo Vecinos, Fortaleciendo Comunidades.</p>", unsafe_allow_html=True)


# Cargar imagen
imagen_path = "./images/vecinonet.png"  # Reemplaza con la ruta de tu imagen
st.image(imagen_path, width=800)



