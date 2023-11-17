# Importo la libreria
import streamlit as st

st.set_page_config(page_title='VecinoNet(Redes para Todos)', page_icon = ':bar_chart:', layout = 'centered')

# Título centradon usando 
st.markdown("<h1 style='text-align: center'>VecinoNet(Redes para Todos)</h1><hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)

# Contenido centrado
st.markdown("<h5 style='text-align: center'>Uniendo Vecinos, Fortaleciendo Comunidades.</h5><hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)


# Cargar imagen
imagen_path = "./images/vecinonet.png"  # Reemplaza con la ruta de tu imagen
st.image(imagen_path, width=800)

st.markdown('En la actualidad, aproximadamente la mitad de la población mundial carece de acceso a Internet, y esta disparidad se acentúa en las áreas rurales de África, Latinoamérica y el sur global.')
st.markdown('En estas regiones, la baja densidad de población y los bajos ingresos ofrecen poco incentivo para el despliegue comercial de infraestructura de red, resultando en zonas que quedan digitalmente excluidas o desatendidas.')
st.markdown('La realidad es que aquellos que residen en estas zonas digitalmente excluidas también enfrentan una serie de desafíos adicionales, que incluyen limitaciones en recursos económicos, oportunidades laborales, acceso a la educación, transporte, suministro de electricidad, igualdad de género, así como dificultades en el acceso a la tierra y al agua potable.')
st.markdown('Estos factores se combinan para crear un panorama complejo de desafíos que afectan la calidad de vida y el desarrollo sostenible en estas comunidades marginadas.')
