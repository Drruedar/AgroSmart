### Contents of the main file ###
import streamlit as st
from PIL import Image

# Tomar nombre de usuario
#====================================
path = 'Ledezma'

# Guardar en un txt para pasarlo como parámetro
#======================================================
with open("path.txt",'w',encoding = 'utf-8') as f:
   f.write(path)


im = Image.open("favico.ico")
st.set_page_config(
    page_title="Hello",
    page_icon=im,layout="wide"
)

st.write("# Welcome to AgroSamart! 👋")

#st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Somos una empresa dedicada al análisis de los datos de tus procesos productivos. Por medio de la revisión minuciosa del dato podemos encontrar patrones ocultos que nos periten determinar qué elementos/variables  pueden ser objeto de revisión para optimizar y mejorar el proceso productivo, con el propósito de generar mayores ganancias optimizando los recursos, haciendo uso eficiente de estos. Este proceso se lleva a cabo por medio de la utilización de tecnología de Inteligencia Artificial de vanguardia, y que ya ha sido probada y validada en varios procesos de producción agrícola.
"""
)

image = Image.open('icono.jpg')

st.image(image, use_column_width = True, caption='by AgroSmart')

image_int = Image.open('integrantes.jpg')

st.image(image_int, use_column_width = True, caption='by AgroSmart')

