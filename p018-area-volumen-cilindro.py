# p018-area-volumen-cilindro
# Calcular el area y volumen de un cilindro 

import math

print('Calcular el area y volumen de un cilindro')
print('Ingresa el radio y la altura separados por un espacio')
r, h = input().split()
r, h = int(r), int(h)

a = math.pi * r * (r + h)#formula para calcular el area
v = math.pi * (r**2) * h#formula para calcular el volumen

print(f'El area del cilindro es {a:.2f} y su volumen es {v:.2f}')
