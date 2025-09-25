# p050-conteo-numeros.py
# Lee números hasta ingresar 999, luego, muestra un resumen estadístico

print('033[2J\033[H')
print('Estadisticas con numeros que el usuario proporciona')

cuenta = 0
suma = 0
cp = cn = cz= 0

while True:
    num = int(input('Introduce un número entero: '))
    if num == 999: 
        print("Detectado código de salida (999)")
        break 
    # Proceso
    cuenta += 1
    suma += num
    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1

print("\n========== REPORTE FINAL ==========")
print(f" Números introducidos: {cuenta}")
print(f" Suma total: {suma}")
print(f" Positivos: {cp}")
print(f" Negativos: {cn}")
print(f" Ceros: {cz}")