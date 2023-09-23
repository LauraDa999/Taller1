# Definir un diccionario que mapea países a sus ciudades capitales en América
capitales_americas = {
    'argentina': 'buenos aires',
    'bolivia': 'la paz',
    'brasil': 'brasilia',
    'canada': 'ottawa',
    'chile': 'santiago',
    'colombia': 'bogota',
    'costa rica': 'san jose',
    'cuba': 'la habana',
    'ecuador': 'quito',
    'el salvador': 'san salvador',
    'estados unidos': 'washington, d.c.',
    'guatemala': 'ciudad de guatemala',
    'honduras': 'tegucigalpa',
    'mexico': 'ciudad de mexico',
    'nicaragua': 'managua',
    'panama': 'ciudad de panama',
    'paraguay': 'asuncion',
    'peru': 'lima',
    'uruguay': 'montevideo',
    'venezuela': 'caracas'
}

# Pedir al usuario que ingrese el nombre de un país en minúsculas
pais = input("Ingrese el nombre del país en minúsculas: ")

# Verificar si el país está en el diccionario y obtener la capital correspondiente
capital = capitales_americas.get(pais, "país no identificado")

# Mostrar la capital o el mensaje de "país no identificado"
print(f"La capital de {pais} es: {capital.capitalize()}")
