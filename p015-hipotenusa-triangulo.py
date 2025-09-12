# p015-hipotenusa-triangulo
# Calcular la hipotenusa de un triangulo rectangulo

import math as mt

print('Dame el cateto adyacente')
a = float(input())
print('Dame el cateto opuesto')
b = float(input())

#Proceso
h = mt.sqrt(a**2 + b**2)

#Salida
print('El triangulo de cateto adyacente', a)
print('El triangulo de cateto opuesto', b)
print(f'Su hipotenusa es: {h:.3f}')
