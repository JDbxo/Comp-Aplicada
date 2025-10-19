#p099-procesar-notas.py
# Programa para leer calificaciones hasta que el usuario introduzca 0

cal = []

while True:
    try:
        cal = float(input('Introduce una nota (0 para terminar): '))
        if cal < 0 or cal > 100:
            print('Error: la nota debe estar entre 0 y 100.')
            continue
        if cal == 0:
            break
        cal.append(cal)
    except ValueError:
        print('Error: introduce un numero valido.')
# Si no se ingreso ninguna nota, finaliza el programa
if len(cal) == 0:
    print('No se introdujeron notas.')
else:
    cant = len(cal)
    s = sum(cal)
    promedio = s / cant
    max = max(cal)
    min = min(cal)

    mn_promedio = [n for n in cal if n < promedio]

    print("\n--- RESULTADOS ---")
    print(f'Cantidad de notas introducidas: {cant}')
    print(f'Lista de notas: {cal}')
    print(f'Suma de las notas: {s:.2f}')
    print(f'Promedio de las notas: {promedio:.2f}')
    print(f'Nota máxima: {max}')
    print(f'Nota mínima: {min}')
    print(f'Notas menores al promedio ({len(mn_promedio)}): {mn_promedio}')
