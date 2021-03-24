import requests
import json

request = requests.get("https://api.sosiva451.com/Ubicaciones/buscar?stringBusqueda=cordoba")

parsed_response = json.loads(request.content)



codigo_partido = parsed_response[0]["value"]["CodigoPartido"]

# Output: 

# "COLON-COR"

