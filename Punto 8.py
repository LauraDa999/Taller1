# Leer la frecuencia en Hertz desde el usuario
frecuencia = float(input("Ingrese la frecuencia en Hertz (Hz): "))

# Definir los límites de las regiones del espectro electromagnético en Hz
radio = (3e2, 3e9)  # 300 Hz a 3 GHz
microondas = (3e9, 3e11)  # 3 GHz a 300 GHz
infrarrojo = (3e11, 4.3e14)  # 300 GHz a 430 THz
visible = (4.3e14, 7.5e14)  # 430 THz a 750 THz
ultravioleta = (7.5e14, 3e16)  # 750 THz a 30 PHz
rayos_x = (3e16, 3e18)  # 30 PHz a 3 EHz
rayos_gamma = (3e18, float('inf'))  # Más de 3 EHz

# Determinar en qué parte del espectro electromagnético se encuentra la frecuencia
if radio[0] <= frecuencia <= radio[1]:
    print("La frecuencia está en la banda de las radiofrecuencias.")
elif microondas[0] <= frecuencia <= microondas[1]:
    print("La frecuencia está en la banda de las microondas.")
elif infrarrojo[0] <= frecuencia <= infrarrojo[1]:
    print("La frecuencia está en la banda de los infrarrojos.")
elif visible[0] <= frecuencia <= visible[1]:
    print("La frecuencia está en la banda de la luz visible.")
elif ultravioleta[0] <= frecuencia <= ultravioleta[1]:
    print("La frecuencia está en la banda de los ultravioletas.")
elif rayos_x[0] <= frecuencia <= rayos_x[1]:
    print("La frecuencia está en la banda de los rayos X.")
elif rayos_gamma[0] <= frecuencia:
    print("La frecuencia está en la banda de los rayos gamma.")
else:
    print("La frecuencia no se encuentra en ninguna banda conocida del espectro electromagnético.")
