import streamlit as st
import pandas as pd
import datetime

import streamlit as st
import matplotlib.pyplot as plt


felinos = pd.read_csv('felinos_filtrado.csv')
st.title("Gráfico")
fig,ax = plt.subplots()

# Crear el gráfico de barras
provincia = felinos['stateProvince'].value_counts()
provincia.plot(kind='bar', ax=ax, color='red')

# Agregar etiquetas y título
ax.set_xlabel('Provincia')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de avistajes de felinos por provincia')

# Mostrar el gráfico
st.pyplot(fig)

