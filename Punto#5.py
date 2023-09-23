import math
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros)
    if n % 2 == 0:
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        mediana = (medio1 + medio2) / 2
    else:
        mediana = numeros_ordenados[n // 2]
    return mediana

def calcular_promedio_multiplicativo(numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto ** (1 / len(numeros))

def ordenar_numeros(numeros, ascendente=True):
    return sorted(numeros) if ascendente else sorted(numeros, reverse=True)

def calcular_potencia_mayor_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def calcular_raiz_cubica_menor(numeros):
    menor = min(numeros)
    return math.pow(menor, 1/3)

numeros = []
for i in range(5):
    numero = float(input(f'Ingrese el número {i + 1}: '))
    numeros.append(numero)

print(f'Promedio: {calcular_promedio(numeros)}')
print(f'Mediana: {calcular_mediana(numeros)}')
print(f'Promedio multiplicativo: {calcular_promedio_multiplicativo(numeros)}')
print(f'Números ordenados de forma ascendente: {ordenar_numeros(numeros)}')
print(f'Números ordenados de forma descendente: {ordenar_numeros(numeros, ascendente=False)}')
print(f'Potencia del mayor número elevado al menor número: {calcular_potencia_mayor_menor(numeros)}')
print(f'Raíz cúbica del menor número: {calcular_raiz_cubica_menor(numeros)}')