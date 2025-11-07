import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng
from streamlit_folium import folium_static, st_folium
import folium

#inicio

st.title("felinos avistados en Argentina")
st.image('images/leo.jpg')
fig,ax = plt.subplots()

st.header("Exploración del archivo CSV")
st.markdown("En esta página exploraremos las columnas más importantes del archivo CSV utilizado.")
st.header("**¿Que es un archivo csv?**")
st.markdown("Un archivo CSV es un archivo de texto plano que almacena datos en formato tabular, como los de una hoja de cálculo o base de datos. En un archivo CSV, cada línea representa una fila y los valores dentro de esa fila están separados por comas (de ahí su nombre: Comma Separated Values o Valores Separados por Comas). ")
st.markdown("**Caracteristicas**")
st.markdown("**Estructura simple:** Es un formato sencillo y universalmente compatible para almacenar y transportar datos tabulares.")
st.markdown("**Compatibilidad:** Se puede abrir y editar con programas de hoja de cálculo como Excel, pero también con editores de texto como el Bloc de notas.")
st.markdown("**Delimitadores:** Aunque la coma es el separador por defecto, también se pueden usar otros caracteres como punto y coma (;), tabulaciones o espacios, dependiendo del programa.")
st.markdown("**Usos comunes:** Se utiliza mucho para importar y exportar datos entre diferentes aplicaciones, organizar información de clientes, o en análisis de datos.")

st.header("previsualizacion del csv")
#st.dataset(felinos)

#mapa

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

#csv
felinos=pd.read_csv('felinos_filtrado.csv')

#selectbox
selection = st.selectbox(
    "Selecciona el criterio:",
    ("genus", "species", 
     "ubicacion", "fechas", "ScientificName")
)

#genus
if selection == "genus":
    genus_s = st.radio(
    "¿Sobre que tipo de felino quiere saber?",
    ["Puma", "Leopardo", "Pantera"])
    if genus_s == "Puma":
        st.title("Puma")
        st.image('images/puma.jpg')
        st.markdown("El puma es un felino grande que habita en casi toda la Argentina, adaptándose a diversos ecosistemas desde la Cordillera de los Andes hasta la Patagonia. Cumple un papel ecológico fundamental como depredador tope, manteniendo el equilibrio de la cadena trófica. Es un animal territorial, solitario y silencioso, capaz de adaptarse a zonas modificadas por el ser humano, aunque su distribución ha sido restringida por la actividad humana en muchas regiones")
    elif genus_s == "Leopardo":
        st.title("Leopardo")
        st.image('images/leopardo.jpeg')
        st.markdown("En Argentina, leopardo se refiere principalmente a dos grandes felinos: el yaguareté (Panthera onca) y el ocelote (Leopardus~pardalis). El yaguareté es el felino más grande de América y tiene manchas en forma de roseta, mientras que el ocelote es más pequeño, adaptable y también tiene un pelaje moteado. ")
    else:
        st.title("Pantera")
        st.image('images/pantera.jpeg')
        st.markdown("La pantera argentina es el yaguareté negro, que no es una especie distinta, sino un yaguareté con melanismo, una condición genética que causa una pigmentación oscura en su pelaje. Los yaguaretés negros son la misma especie que el yaguareté común (Pantheraonca), y en Argentina se han reportado avistamientos en Misiones y las Yungas salteñas, aunque no hay confirmación oficial. ")
#species
elif selection == "species":
    st.markdown("species")
    especies=felinos['species'].value_counts()
    with st.container(border=True):
        animal = st.multiselect("Especies de felinos", especies, default=especies)
        if animal:
            filtro=felinos[felinos['especies'].isin(animal)]

    #tab1, tab2 = st.tabs(["Chart", "Dataframe"])
    #tab1.line_chart(felinos, height=250)
    #tab2.dataframe(felinos, height=250, use_container_width=True)
#ubicacion
elif selection == "ubicacion":
    st.title("Mapa")
    st.markdown("En este mapa veremos los avistajes de tres géneros de felinos.")

    mapa = generar_mapa()

    def agregar_marca_aerop(row):
        #st.write(color)
        folium.Marker(
            [row['lat'], row['lng']],
            popup=row['locality'],
            icon=folium.Icon(color='blue')
        ).add_to(mapa)

    ac1,ac2 = st.columns([0.3, 0.7])

    r_puma = ac1.checkbox("puma")
    if r_puma:
        a_larg = felinos[felinos['genus']=='Puma']
        a_larg.apply(agregar_marca_aerop, axis=1)
    r_leopardo = ac1.checkbox("leopardo")
    if r_leopardo:
        a_med = felinos[felinos['genus']=='Leopardus']
        a_med.apply(agregar_marca_aerop, axis=1)
    r_pantera = ac1.checkbox("pantera")
    if r_pantera:
        a_small = felinos[felinos['genus']=='Panthera']
        a_small.apply(agregar_marca_aerop, axis=1)

    with ac2:
        st_folium(mapa, key='felinos')

elif selection == "fechas":
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
#nombre cientifico
else:
    st.write("ScientificName")

st.write("You selected:",selection)