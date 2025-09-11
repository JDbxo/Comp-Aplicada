# p009-promedio-de-calificaciones
# Objetivo: Calcular el promedio de tres calificaciones ingresadas por el usuario.

print('Calculando el promedio de tres calificaciones:\n')

# Solicitar las 3 calificaciones en una sola línea separadas por espacio
print('Dame 3 calificaciones separadas por espacios:')
cal1, cal2, cal3 = input().split()
print(type(cal1), type(cal2), type(cal3))

cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3) #Se convierten las variables de cadena a entero 
print(type(cal1), type(cal2), type(cal3))

# Calcular el promedio
suma = (cal1 + cal2 + cal3)
promedio = suma / 3

# Mostrar el resultado incluyendo las calificaciones
print(f'Las calificaciones son: {cal1}, {cal2}, {cal3}')
print (f'La suma es: {suma}')
print(f'El promedio de las calificaciones es: {promedio}')