import re
import unicodedata

def normalizar(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sem_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sem_acentos)
    return texto_limpo.lower()

def validar_numero_telefone(numero):
    padrao = r'^(\d{10}|\d{11})$'
    return bool(re.match(padrao, numero))
