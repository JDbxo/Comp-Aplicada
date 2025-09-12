# p019-calculo-tiempo
# Convertir horas en días, minutos y segundos

print('Convertir horas en dias, minnutos y segundos')
print('Introduce la cantidad de horas en numero entero')
horas = int(input())

#Proceso
dias = horas // 24 # División entera para días completos
minutos = horas * 60
seg = horas * 60 * 60

# Salida
print(f'{horas} horas equivalen a: \n')
print(f'{dias} día(s)\n')
print(f'{minutos} minuto(s)\n')
print(f'{seg} segundo(s)\n')