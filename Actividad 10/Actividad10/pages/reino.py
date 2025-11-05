import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_folium import folium_static, st_folium
from numpy.random import default_rng as rng

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- App title & image ---
st.title("Felinos avistados en Argentina")
st.image('images/leo.jpg')

# --- Read CSV ---
felinos = pd.read_csv('felinos_filtrado.csv')

# --- Map generator ---
def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )

    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'

    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m

# --- Selection box ---
selection = st.selectbox(
    "Selecciona el criterio:",
    ("kingdom", "phylum", "class", "order", "family", "genus", "species", 
     "ubicacion", "fechas", "taxonKey", "ScientificName")
)

# --- If user selects "ubicacion" ---
if selection == "ubicacion":
    st.title("Mapa")
    st.markdown("En este mapa veremos los avistajes de tres géneros de felinos.")

    mapa = generar_mapa()  # create map before adding markers

    # Function to add markers to map
    def agregar_marca_aerop(row):
        folium.Marker(
            [row['lat'], row['lng']],
            popup=row['locality'],
            icon=folium.Icon(color='blue')
        ).add_to(mapa)

    # Two-column layout
    ac1, ac2 = st.columns([0.3, 0.7])

    with ac1:
        r_puma = st.checkbox("Puma")
        r_leopardus = st.checkbox("Leopardus")
        r_panthera = st.checkbox("Panthera")

    # Add markers depending on checkboxes
    if r_puma:
        felinos[felinos['genus'] == 'Puma'].apply(agregar_marca_aerop, axis=1)
    if r_leopardus:
        felinos[felinos['genus'] == 'Leopardus'].apply(agregar_marca_aerop, axis=1)
    if r_panthera:
        felinos[felinos['genus'] == 'Panthera'].apply(agregar_marca_aerop, axis=1)

    with ac2:
        st_folium(mapa, key='felinos_map')

else:
    st.write("Nada seleccionado.")

st.write("You selected:", selection)
