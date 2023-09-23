# Taller1

#  1.El resultado de nuestro Python Beginner Quiz:
![image](https://github.com/LauraDa999/Taller1/assets/141860731/66ca48a6-5a2f-4997-ac10-2e6b19232d5a)

# 2. Realice un programa que lea tres números reales y determine cuál es el mayor.
```
n1 = int(input("ingrese el primer número"))
n2 = int(input("ingrese el segundo número"))
n3 = int(input("ingree el tercer número"))
if n1 and n1 > n3:
    print("El número mayor es: ",n1) 
elif n2 > n1 and n2 > n3:
    print("El número mayor es:",n2)
elif n3 > n1 and n3 > n2:
    print("El número mayor es: ",n3)
else:
    print("No se pudo establecer el mayor")
```


#  Diagrama de flujo
![diagrama](https://github.com/LauraDa999/Taller1/blob/main/Diagrama%20Taller%201.jpg?raw=true)


# 3. Realice un programa que lea un número enteros y determine si es par o impar.
```


numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

```

# 4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
```
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero2 == 0:
    print("No se puede determinar si un número es múltiplo de cero.")
else:
    if numero1 % numero2 == 0:
        print(f"{numero1} es múltiplo de {numero2}.")
    else:
        print(f"{numero1} no es múltiplo de {numero2}.")
```

# 5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
```
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
```

# 6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante
```
c = input("Ingresa una letra cualquiera: ")
vocales =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if c in vocales:
    print("Es una vocal") 
else:     
    print("Es una consonante")
```
    
# 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

-El promedio
-La mediana
-El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
-Ordenar los números de forma ascendente
-Ordenar los números de forma descendente
-La potencia del mayor número elevado al menor número
-La raíz cúbica del menor número

```
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
```

# 8. Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

![image](https://github.com/LauraDa999/Taller1/assets/141860731/69078ae9-4e80-4e88-99bf-40dbb16d888f)

#  9. Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.

![image](https://github.com/LauraDa999/Taller1/assets/141860731/2e986443-055d-4605-9370-18cc49f5cf2e)


#  10. Escriba un programa que dada una distancia calcule:

El tiempo que le tomaría a la luz recorrer la distancia.
El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
El tiempo que le tomaría a Bolt recorrer la distancia.

![image](https://github.com/LauraDa999/Taller1/assets/141860731/a8c1d073-60a8-4d83-a064-0dcb251b7025)








