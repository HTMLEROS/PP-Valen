import pandas as pd
import streamlit as st

felinos=pd.read_csv('felinos_filtrado.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
st.markdown("El dataset cuenta con muchos datos como las provincias, los dias avistados, entre otros. Destacaremos los mas importantes")
filas, columnas = felinos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = felinos.shape
    st.markdown(f'Tiene { filas} filas y {columnas} columnas')
    
    
provincia = felinos['stateProvince'].unique()
genus = felinos['genus'].unique()

with st.expander("¿Cuántos y cuales son los valores únicos de la columna **genus**?"):
    st.markdown("cuenta con:")
    st.markdown(genus)

with st.expander("¿Cuáles son los valores únicos de la columna **stateProvince**?"):
    st.markdown("Las provincias en las que se avistaron pumas son:")
    st.markdown(provincia)

with st.expander("¿Cuáles son los nombres de las columnas ?"):
    st.markdown("las columnas se llaman:")
    st.markdown(felinos.columns)