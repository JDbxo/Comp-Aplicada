# p016-tercer-angulo
#Calculadora del tercer angulo de un triangulo 

import math as mt

print('Calcula el tercer angulo de un triangulo')

#Conociendo dos angulos 
# Los angulos a+b<180
print('Dame el primer y segundo angulo separados por un espacio')
ang_a, ang_b = input().split()
ang_a, ang_b = float(ang_a), float(ang_b)

#Proceso
ang_c = 180 - (ang_a + ang_b)

print(f'El tercer angulo conociendo dos angulos es: {ang_c}')