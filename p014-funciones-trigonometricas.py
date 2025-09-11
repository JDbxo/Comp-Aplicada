# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas básicas

import math as mt

# Definir un ángulo en grados y convertirlo a radianes
angulo = 90
radianes = mt.radians(angulo)

# Calcular funciones trigonométricas básicas
seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

# Convertir de vuelta a grados para demostración
grados = mt.degrees(radianes)

# Formatear la salida con f-strings para mejor presentación
salida = ('Resumen de funciones\n'
f'El seno es: {seno:.4f}\n'
f'El coseno es: {coseno:.4f}\n'
f'La tangente es: {tangente:.4f}\n'
f'El angulo {angulo} grados, equivale a {radianes:.4f} radianes\n'
f'Los {radianes:.4f} radianes equivalen a {grados:.1f}°\n')

# Mostrar la salida formateada
print(salida)