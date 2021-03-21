import requests
#from requests_html import HTMLSession
from bs4 import BeautifulSoup
# import json

# url = "https://www.argenprop.com/"

# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')

#home_ubicacion_button = soup.find_all(id="home-ubicacion")

#string_locacion = "tandil"

#url_busqueda = f"https://api.sosiva451.com/Ubicaciones/buscar?stringBusqueda={string_locacion}"

#locacion_busqueda = requests.get(url_busqueda)

#primer_item_busqueda = json.loads(locacion_busqueda.content)[0]

tipo_operacion = "alquiler"
tipo_propiedad = "departamento"
partido = "tandil" # primer_item_busqueda["value"]["NombrePartido"]

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

searchear_partido = requests.post("https://www.argenprop.com/Home/Search", data=payload)

#session = HTMLSession()

#searchear_partido = session.post("https://www.argenprop.com/Home/Search", data=payload)

# archivo = open(r"C:\Users\nicol\repos\ArgenProp_Scrapping\nicolargenprop.html", "w")
# archivo.write(searchear_partido.text)
# archivo.close()

soup = BeautifulSoup(searchear_partido.text, 'lxml')

lista_raw_resultado_busqueda = soup.find_all("div", {"class": "listing__item listing__item--featured"})

# bloque_items = soup.find_all("div", {"class": "listing-container"})

bloque_items = soup.find_all("div", {"class": "listing__item"})

class Objeto_ArgenProp:
    def __init__(self, titular, link, fotos, monto, direccion, descripcion):
        self.titular = titular
        self.link = f"https://www.argenprop.com{sublink}"
        self.fotos = fotos
        self.monto = monto
        self.direccion = direccion
        self.descripcion = descripcion

lista_objetos_argenprop = []

for objeto in bloque_items:
    titular = objeto.find("h3").get("title")
    sublink = objeto.find("a").get("href")
    html_fotos = objeto.find_all("img")
    fotos = []
    for img in html_fotos:
        fotos.append(img.get("data-src"))
    monto = int(objeto.find("p").text.strip()[2:].replace(".", ""))
    direccion = objeto.find("h2").text.strip()
    descripcion = objeto.find("p", {"class": "card__info"}).text.strip()
    objeto_argenprop = Objeto_ArgenProp(titular=titular, link=sublink, fotos=fotos, monto=monto, direccion=direccion, descripcion=descripcion)
    lista_objetos_argenprop.append(objeto_argenprop)

count = 1
for arg_objeto in lista_objetos_argenprop:
    print(f"{count} | {arg_objeto.titular} | {arg_objeto.link} | ${arg_objeto.monto}")
    count += 1

# OUTPUT:

# 1 | Duplex en ALQUILER, 2 dormitorios | https://www.argenprop.com/departamento-en-alquiler-en-tandil--8534105 | $22000
# 2 | EN ALQUILER DEPARTAMENTO 1 DORMITORIO TANDIL | CENTRICO | https://www.argenprop.com/departamento-en-alquiler-en-tandil-2-ambientes--7338270 | $19000
# 3 | SE ALQUILA DEPARTAMENTO DOS DORMITORIOS | TANDIL | https://www.argenprop.com/departamento-en-alquiler-en-tandil-3-ambientes--8538044 | $22500
# 4 | EN ALQUILER DEPARTAMENTO 1 DORMITORIO TANDIL | DEL VALLE 400 | https://www.argenprop.com/departamento-en-alquiler-en-tandil-2-ambientes--6191171 | $12500