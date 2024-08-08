
try:
    numero = 10
    errors = []
    if numero < 0:
        errors.append('Número não pode ser negativo')
    
    if numero.is_integer():
        errors.append('Número não pode ser inteiro')
    
    if numero % 2 == 0:
        errors.append('Número não pode ser par')
    
    if errors:
        raise Exception(errors)
    
except Exception as error:
    for erro in errors:
        print('ERROR:', erro)