import streamlit as st
import pandas as pd

st.image('images/banner.png')

st.title("Aanálisis de Datos en la Facultad de Informática")
st.subheader(" Con Python🐍")
st.write("¿Qué sabemos de (completar sobre los datos seleccionados)...")

#etapa 1
st.subheader("Exploracion básica")

felinos=pd.read_csv('felinos_filtrado.csv')
st.write("trabajare con el csv de felinos")
felinos