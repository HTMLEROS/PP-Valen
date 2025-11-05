import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng

st.title("felinos avistados en Argentina")
st.image('images/leo.jpg')
fig,ax = plt.subplots()

felinos=pd.read_csv('felinos_filtrado.csv')

options = ["kingdom", "phylum", "class", "order", "family", "genus", "species", "ubicacion", "fechas", "taxonKey", "ScientificName"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")
