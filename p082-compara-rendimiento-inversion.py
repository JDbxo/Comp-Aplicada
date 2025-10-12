#p082-compara-rendimiento-inversion.py
# Compara el rendimiento de dos fondos de inversión

print('Fondo de Inversión A ')
montoA = float(input('Monto inicial: '))
tasaA = float(input('Tasa de interes anual (%): '))

print('\nFondo de Inversión B')
montoB = float(input('Monto inicial: '))
tasaB = float(input('Tasa de interes anual (%): '))

an = int(input('\nAños a proyectar: '))

print('\n   Comparacion de Rendimientos Anuales    ')
print('Año |  Fondo A   |  Fondo B')
print('-------------------------------')

fondoA = montoA
fondoB = montoB

for i in range(1, an + 1):
    fondoA = fondoA * (1 + tasaA / 100)
    fondoB = fondoB * (1 + tasaB / 100)
    print(f"{i:2d}  |  ${fondoA:8.2f}  |  ${fondoB:8.2f}")

print('\nResultado final:')

if fondoA > fondoB:
    print(f'El Fondo A (${fondoA:.2f}) supero al Fondo B (${fondoB:.2f}).')
elif fondoB > fondoA:
    print(f'El Fondo B (${fondoB:.2f}) supero al Fondo A (${fondoA:.2f}).')
else:
    print(f'Ambos fondos terminaron con el mismo valor: ${fondoA:.2f}.')
