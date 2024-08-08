import json

carros_dict = {"marca": "Ford", "modelo": "Fusion", "ano": 2013}
carros_dict2 = {"marca": "fiat", "modelo": "uno", "ano": 2013}
carros_dict3 = {"marca": "fiat", "modelo": "uno", "ano": 2013}
carros_dict4 = {"marca": "fiat", "modelo": "uno", "ano": 2013}

# dictioanry -> objecto JSON

carros_list = ["Ford", "Fusion", 'fiat']
# list -> array JSON

carros_tupla = ("Ford", "Fusion", 'fiat')
# tupla -> array JSON


carros_j = json.dumps([carros_dict, carros_dict2, carros_dict3, carros_dict4], indent=2, separators=(":", " = "), sort_keys=True)
# indent=2 -> identação de 2 espaços
# separators=(":", " = ") -> Troca o separador padrão por ": " e " = "
# sort_keys=True -> Ordena as chaves do dicionário
print(carros_j)