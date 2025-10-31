import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

felinos = pd.read_csv('felinos_filtrado.csv')
st.title("Gráfico")
st.markdown("Este gráfico nos muestra la cantidad de avistajes por provincia")
fig,ax = plt.subplots()

#arreglo de Neuquen
col_replace = {'Neuquén / Río Negro' : 'Neuquén', 'Neuquen' : 'Neuquén'}

#evitar errores
felinos_c = felinos.copy()
felinos_c['stateProvince'] = felinos_c['stateProvince'].replace(col_replace)

# Crear el gráfico de barras
provincia = felinos_c['stateProvince'].value_counts()
provincia.plot(kind='bar', ax=ax, color='red')

# Agregar etiquetas y título
ax.set_xlabel('Provincia')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de avistajes de felinos por provincia')

# Mostrar el gráfico
st.pyplot(fig)

