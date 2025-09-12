# p020-numero-suerte
# Descompone el año de nacimiento y suma sus dígitos

print('Ingresa tu año de nacimiento (4 dígitos cada uno separado por un espacio): ')
a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

#Proceso
suma = a + b + c + d

#Salida
print(f'El año es {a}{b}{c}{d}')
print(f'La suma de los dígitos es: {suma}')