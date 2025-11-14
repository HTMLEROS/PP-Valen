import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng
from streamlit_folium import folium_static, st_folium
import folium

felinos = pd.read_csv('felinos_filtrado.csv')

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
st.dataframe(felinos)

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

#selectbox
selection = st.selectbox(
    "Selecciona el criterio:",
    ("genus", "species", 
     "ubicacion")
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
        with st.expander("Caza"):
        	st.markdown("A los pumas les gusta cazar ciervos, aunque también comen animales más pequeños como los coyotes, puercoespines y mapaches. Suelen cazar de noche o durante las horas del amanecer y el anochecer. Estos felinos emplean una mezcla de sigilo y poder, acechan a su presa hasta que llega la oportunidad de saltar, y luego atacan la nuca con un mordisco fatal. Esconderán cadáveres grandes y se alimentarán de ellos durante varios días.")
        with st.expander("Comportamiento"):
        	st.markdown("Los pumas necesitan mucho espacio: solo unos pocos felinos pueden sobrevivir en un rango de 77 kilómetros cuadrados. Son animales solitarios y tímidos, pocas veces vistos por los seres humanos. Si bien esporádicamente atacan a personas, generalmente niños o adultos solitarios, las estadísticas muestran que, en promedio, solo hay cuatro ataques y una muerte humana cada año en todos los EE. UU. y Canadá")
        with st.expander("Hábitat"):
        	st.markdown("El puma habita en una vasta gama de ecosistemas en América, desde los bosques de Canadá hasta los Andes en América del Sur, incluyendo bosques, praderas, desiertos, montañas, selvas y matorrales. Se adapta a diferentes ambientes, aunque evita las áreas agrícolas y prefiere lugares con cobertura vegetal, cuevas y grietas rocosas para refugiarse.")
    elif genus_s == "Leopardo":
        st.title("Leopardo")
        st.image('images/leopardo.jpeg')
        st.markdown("En Argentina, leopardo se refiere principalmente a dos grandes felinos: el yaguareté (Panthera onca) y el ocelote (Leopardus~pardalis). El yaguareté es el felino más grande de América y tiene manchas en forma de roseta, mientras que el ocelote es más pequeño, adaptable y también tiene un pelaje moteado. ")
        st.markdown("Es uno de los felinos más atractivos directamente emparentado con los jaguares, los guepardos, los tigres y los leones. Como gran y experto depredador, le gusta llevarse a sus presas a las alturas de los árboles, donde se sienten muy cómodos. Allí mantiene la caza a salvo de los posibles carroñeros que a menudo merodean alrededor de sus víctimas.")
        with st.expander("Caza"):
        	st.markdown("Generalmente cazan de noche, la mayoría de los ejemplares habitan en los bosques, selvas y sabanas africanas, aunque también hay algunos en Asia central, India y China. Pueden llegar a medir casi dos metros de largo y pesan entre 30 y 90 kilos, tienen garras retráctiles que les permiten agarrarse con fuerza a la tierra y al tronco de los árboles para trepar en ellos. ")
        with st.expander("Comportamiento"):
        	st.markdown("Viven y cazan solos, evitando la compañía de otros leopardos salvo para aparearse o criar a sus cachorros. Son cazadores sigilosos, aprovechando la noche y el camuflaje para acechar y emboscar a una gran variedad de presas. Su distintivo hábito de arrastrar las presas a las ramas de los árboles les permite proteger su comida de otros depredadores. Su capacidad para prosperar en diversos hábitats, desde selvas hasta desiertos, demuestra su notable versatilidad y resiliencia.")
        with st.expander("Hábitat"):
        	st.markdown("El leopardo (Panthera pardus) posee el hábitat más extenso y versátil de todos los grandes felinos, distribuido a lo largo de África y Asia. Su gran capacidad de adaptación le permite prosperar en una diversidad de entornos que van desde sabanas y selvas tropicales hasta zonas montañosas, matorrales, y áreas semiáridas. Son animales solitarios y oportunistas que requieren principalmente dos elementos en su hábitat: una fuente adecuada de alimento (presas) y cobertura vegetal o rocosa (árboles, cuevas, maleza) para esconderse y cazar de forma eficaz. Esta flexibilidad ecológica explica su amplia dispersión geográfica.")
    else:
        st.title("Pantera")
        st.image('images/pantera.jpeg')
        st.markdown("El término pantera no es exclusivo de un animal. De hecho, según Panthera Project, una ONG internacional sin fines de lucro que trabaja para conservar las 40 especies de felinos salvajes del mundo y los vastos ecosistemas que habitan, la palabra se remonta a la clasificación taxonómica (género Panthera) de todos los grandes felinos (principalmente tigres, leones, jaguares y leopardos).")
        st.markdown("Por tanto, la pantera negra no es más que un gran felino de pelaje negro. Según el proyecto, lo que sucede es un fenómeno llamado melanismo, caracterizado por una producción excesiva, concentrada y considerable del pigmento negro melanina en el pelaje de los gatos salvajes.")
        st.markdown("Entonces, tanto un jaguar como un leopardo pueden ser lo que se llama una pantera negra. Sin embargo, no todas las especies del género Panthera pueden ser negras.")
        with st.expander("Los jaguares y los leopardos son las panteras negras más comunes."):
        	st.markdown("Los felinos en los que se observa con mayor frecuencia el melanismo son los jaguares (Panthera onca), comunes en América, y los leopardos (Panthera pardus) de África y Asia.")
        	st.markdown("No es solo porque estos animales tienen un color oscuro que no tiene manchas, sino porque además son más difíciles de ver ya que está más mezclado con el color del resto del pelaje.")
        with st.expander("La mayoría de las panteras negras viven en el Amazonas y en los bosques de Asia y África"):
        	st.markdown("El rango de ocurrencia de los jaguares, en general, se encuentra en las Américas, desde el norte de México hasta el norte de Argentina. Según la ONG internacional, los jaguares negros pueden habitar muchos lugares, pero se sabe que la mayoría de las panteras negras se encuentran en la Amazonía, en la selva tropical profunda.")
        	st.markdown("Los leopardos negros habitan tanto en Asia como en África. Según el proyecto, las panteras negras africanas son solitarias, misteriosas y difíciles de encontrar y, a menudo, se quedan en los árboles donde la gente no puede verlas.")
        with st.expander("En Argentina"):
        	st.markdown("En Argentina no habitan especies nativas que se clasifiquen formalmente como leopardos o panteras en el sentido estricto de las especies del género Panthera que viven en África y Asia (como el leopardo africano o la pantera negra). Sin embargo, el término pantera se usa a menudo localmente para referirse al yaguareté, y la palabra leopardo se usa a veces para los felinos manchados más pequeños.")
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
    st.markdown("En este mapa veremos los avistajes de tres géneros de felinos, filtrados por año.")

    # Maximo y Minimo sacando los nan
    min_year = int(felinos['year'].dropna().min())
    max_year = int(felinos['year'].dropna().max())

    # slider
    selected_years = st.slider(
        "Seleccione un rango de años",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # filtro y para el mapa
    filtered_felinos_by_year = felinos[
        (felinos['year'] >= selected_years[0]) & (felinos['year'] <= selected_years[1])
    ]

    mapa = generar_mapa()

    def agregar_marca_aerop(row):
        folium.Marker(
            [row['lat'], row['lng']],
            popup=f"{row['locality']} ({int(row['year'])})", # Add year to popup
            icon=folium.Icon(color='blue')
        ).add_to(mapa)

    ac1,ac2 = st.columns([0.3, 0.7])

    r_puma = ac1.checkbox("puma")
    if r_puma:
        a_larg = filtered_felinos_by_year[filtered_felinos_by_year['genus']=='Puma']
        a_larg.apply(agregar_marca_aerop, axis=1)
    r_leopardo = ac1.checkbox("leopardo")
    if r_leopardo:
        a_med = filtered_felinos_by_year[filtered_felinos_by_year['genus']=='Leopardus']
        a_med.apply(agregar_marca_aerop, axis=1)
    r_pantera = ac1.checkbox("pantera")
    if r_pantera:
        a_small = filtered_felinos_by_year[filtered_felinos_by_year['genus']=='Panthera']
        a_small.apply(agregar_marca_aerop, axis=1)

    with ac2:
        st_folium(mapa, key='felinos')

else:
    # Crear el gráfico de barras
    especies = felinos['species'].value_counts()
    especies.plot(kind='pie', ax=ax)

    # Agregar etiquetas y título
    ax.set_title('Cantidad de avistajes de felinos por provincia')

    # Mostrar el gráfico
    st.pyplot(fig)
#nombre cientifico

st.write("You selected:",selection)