# p032-aceptar-estudiante.py
# Aceptar a un estudiante en base a la edad y calificaciones con or.
print('\033[2J\033[H')
print('Admisiones a la Universidad ')
nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad < 18:
    print(f' Lo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.')
else:

    print('Ingresa 2 calificaciones para continuar:')
    calificacion1 = float(input())
    calificacion2 = float(input())

if calificacion1 < 8 or calificacion2 < 8:
    print(' Lo sentimos, se requiere una calificación mínima de 8 en ambos exámenes.')
else:

    print(f' ¡Bienvenid@, {nombre}! Tu edad de {edad} y tus calificaciones te permiten ingresar.')