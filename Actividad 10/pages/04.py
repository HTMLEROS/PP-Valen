import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

felinos=pd.read_csv('felinos_filtrado.csv')

st.title("Informacion sobre felinos avistados en la Argentina")
st.image('images/leo.jpg')

st.subheader("¿Que desea saber?")

#seleccionador
columnas = st.selectbox(
    "¿Que desea saber?",
    ("kingdom", "phylum", "class", "order", "family", "genus", "species", "locality", "stateProvince", "lat", "lng", "elevation",
       "day", "month", "year", "taxonKey", "ScientificName",
       "VernacularNames"),
)

st.write("You selected:", columnas)

genus = len(felinos['genus'].unique())
avis = len(felinos['day'].value_counts())

felinos(
    {
        genus: ["Puma", "Leopardus", "Panthera"],
        "c. de avistamientos": rng(0).integers(0, 1000, size=3),
        "dias avistados": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.dataframe(
    felinos,
    column_config={
        genus: "tipo",
        "day": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)