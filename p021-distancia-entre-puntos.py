# p021-distancia-entre-puntos
# Calcular distancia entre dos puntos en el plano cartesiano 

import math

print('Introduce las coordenadas del punto A separadas por un enter: ')
x1 = float(input())
y1 = float(input())
print('\nIntroduce las coordenadas del punto B separadas por un enter:')
x2 = float(input())
y2 = float(input())

#Proceso
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f"\nLa distancia entre el punto A de coordenadas ({x1}, {y1}) y el punto B de cordenadas({x2}, {y2}) es: {d:.2f}")