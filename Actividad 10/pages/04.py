import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng

st.title("felinos avistados en Argentina")
st.image('images/leo.jpg')
fig,ax = plt.subplots()

felinos=pd.read_csv('felinos_filtrado.csv')

años=felinos['year'].value_counts()
st.write(años)

# Crear el gráfico de barras
años.plot(kind='bar', ax=ax, color='red')

# Agregar etiquetas y título
ax.set_xlabel('year')
ax.set_ylabel('avistajes')
ax.set_title('Cantidad de avistajes de felinos por provincia')

# Mostrar el gráfico
st.pyplot(fig)