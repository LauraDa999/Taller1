# Leer dos números reales desde el usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Verificar si el segundo número es cero
if numero2 == 0:
    print("No se puede determinar si un número es múltiplo de cero.")
else:
    # Verificar si el primer número es múltiplo del segundo
    if numero1 % numero2 == 0:
        print(f"{numero1} es múltiplo de {numero2}.")
    else:
        print(f"{numero1} no es múltiplo de {numero2}.")
