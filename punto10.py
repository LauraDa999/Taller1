velocidad_luz = 299792458  # Velocidad de la luz en el vacío
velocidad_sonido_aire = 343  # Velocidad del sonido en el aire a temperatura ambiente
velocidad_avion_comercial = 250  # Velocidad promedio de un avión comercial en m/s
velocidad_bolt = 12.42  # Velocidad máxima registrada de Usain Bolt en m/s

distancia = float(input("Ingrese la distancia en metros: "))

tiempo_luz = distancia / velocidad_luz
tiempo_sonido_aire = distancia / velocidad_sonido_aire
tiempo_avion_comercial = distancia / velocidad_avion_comercial
tiempo_bolt = distancia / velocidad_bolt

print(f"Tiempo que tomaría a la luz recorrer la distancia: {tiempo_luz:.6f} segundos")
print(f"Tiempo que tomaría al sonido en el aire recorrer la distancia: {tiempo_sonido_aire:.6f} segundos")
print(f"Tiempo que tomaría al vehículo comercial más veloz recorrer la distancia: {tiempo_avion_comercial:.6f} segundos")
print(f"Tiempo que tomaría a Usain Bolt recorrer la distancia: {tiempo_bolt:.6f} segundos")
