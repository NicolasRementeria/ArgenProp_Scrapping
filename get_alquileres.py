import requests
from bs4 import BeautifulSoup

tipo_operacion = "alquiler"
tipo_propiedad = "departamento"
partido = "CORDOBA-CAPITAL" # Resultado de get_codigo_partido.py

payload = {
    "LocationSearch.ViewMap": "",
    "LocationSearch.LocationFieldName": "",
    "LocationSearch.LocationFieldValue": "",
    "LocationSearch.TipoOperacion": tipo_operacion,
    "LocationSearch.TipoPropiedad": tipo_propiedad,
    "LocationSearch.LocationTerm": "",
    "LocationSearch.partido": partido
}

busqueda_argenprop = requests.post("https://www.argenprop.com/Home/Search", data=payload)

soup = BeautifulSoup(busqueda_argenprop.text, 'lxml')

lista_raw_resultado_busqueda = soup.find_all("div" , {"class": "card__photos-box"})

try:
    sublink_url_next_page = soup.find("li", {"class": "pagination__page-next pagination__page"}).find("a").get("href")
    conformed_next_page_url = f"https://www.argenprop.com/{sublink_url_next_page}"
except:
    conformed_next_page_url = "NONE"

## CREAR LISTA DONDE CADA ITEM SEA UN ALQUILER CONCRETO
## APPENDEAR A LA LISTA TODOS LOS ALQUILERES DE TODAS LAS PAGINAS