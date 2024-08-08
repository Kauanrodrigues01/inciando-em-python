carros = ['HRV', 'Polo', 'Civic', 'Golf', 'Argo', 'Onix', 'Creta', 'Corolla', 'Compass', 'Cruze']
itCarros = iter(carros)

while True:
    try:
        print(next(itCarros))
    except StopIteration:
        break