import pandas as pd
import streamlit as st

felinos=pd.read_csv('felinos_filtrado.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
filas, columnas = felinos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = felinos.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
provincia = felinos['stateProvince'].unique()
genus = len(felinos['genus'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna **genus**?"):
    st.write(genus)

with st.expander("¿Cuáles son los valores únicos de la columna **stateProvince**?"):
    st.write(provincia)

with st.expander("¿Cuáles son los nombres de las columnas ?"):
   
    st.write(felinos.columns)