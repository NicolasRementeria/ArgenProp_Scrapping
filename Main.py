import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json

url = "https://www.argenprop.com/"

r = requests.get(url)
#soup = BeautifulSoup(r.text, 'lxml')
soup = BeautifulSoup(r.text, 'html.parser')
home_ubicacion_button = soup.find_all(id="home-ubicacion")

string_locacion = "tandil"

url_busqueda = f"https://api.sosiva451.com/Ubicaciones/buscar?stringBusqueda={string_locacion}"

locacion_busqueda = requests.get(url_busqueda)

primer_item_busqueda = json.loads(locacion_busqueda.content)[0]

tipo_operacion = "alquiler"
tipo_propiedad = "departamento"
partido = primer_item_busqueda["value"]["NombrePartido"]

payload = {
    "LocationSearch.ViewMap": "",
    "LocationSearch.LocationFieldName": "",
    "LocationSearch.LocationFieldValue": "",
    "LocationSearch.TipoOperacion": tipo_operacion,
    "LocationSearch.TipoPropiedad": tipo_propiedad,
    "LocationSearch.LocationTerm": "",
    "LocationSearch.partido": partido
}

#LocationSearch.ViewMap=&LocationSearch.LocationFieldName=&LocationSearch.LocationFieldValue=&LocationSearch.TipoOperacion=alquiler&LocationSearch.TipoPropiedad=departamento&LocationSearch.LocationTerm=&LocationSearch.partido=tandil


#searchear_partido = requests.post("https://www.argenprop.com/Home/Search", data=payload)

session = HTMLSession()

searchear_partido = session.post("https://www.argenprop.com/Home/Search", data=payload)


archivo = open(r"C:\Users\nicol\repos\ArgenProp_Scrapping\nicolargenprop.html", "w")
archivo.write(searchear_partido.text)
archivo.close()