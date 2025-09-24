# p31-2da-ley-de-newton.py
# Calcular fuerza, masa o aceleración según la elección del usuario.

print('Calculadora de la 2da Ley de Newton')
print('[F] Calcular la Fuerza (fuerza = masa * aceleración)')
print('[M] Calcular la Masa (masa = fuerza / aceleración)')
print('[A] Calcular la Aceleración (aceleración = fuerza / masa)')
opcion = input('Elige una opción (F, M o A): ').upper()

# La estructura if/elif/else ejecuta el cálculo correcto
if opcion == 'F':
    print('\n Calculando la Fuerza...')
    masa = float(input('masa: '))
    aceleracion = float(input('aceleración: '))
    fuerza = masa * aceleracion
    print(f' La fuerza es: {fuerza} ')
elif opcion == 'M':
    print('\n Calculando la Masa...')
    fuerza = float(input('fuerza: '))
    aceleracion = float(input('aceleración: '))
    masa = fuerza / aceleracion
    print(f' La masa es: {masa} ')
elif opcion == 'A':
    print('\n Calculando la Aceleración...')
    fuerza = float(input('fuerza: '))
    masa = float(input('masa: '))
    aceleracion = fuerza / masa
    print(f' La aceleración es: {aceleracion} ')
else:
    print('\n Opción inválida. Por favor, elige F, M o A.')