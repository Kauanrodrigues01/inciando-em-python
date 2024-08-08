import json

carros = {"marca": "Ford", "modelo": "Fusion", "ano": 2013}

carros_json = json.dumps(carros)
print(carros_json)