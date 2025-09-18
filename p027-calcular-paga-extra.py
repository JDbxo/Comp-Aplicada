# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.

print("\033[2J\033[H", end="")#Borra los datos de la terminal clc
print('Calculando la paga de un trabajador ')

# Entrada
print("Introduce los datos del trabajador: \n")
nombre = input('Nombre del trabajador: ')
horas = int(input('Horas trabajadas: '))
paga_hora = float(input('Paga por hora: '))

# Cálculo de la paga
horas_normales = 50
horas_extra = 0
paga_normal = 0
paga_extra = 0
total = 0

paga_normal = horas_normales * paga_hora
horas_extra = paga_extra = 0
horas_extra = horas - 40
paga_extra = horas_extra * (paga_hora * 2)
total = paga_normal + paga_extra

if horas <= horas_normales:
    paga_normal = horas_normales * paga_hora
    total = paga_normal
else:
    paga_normal = horas_normales * paga_hora
    horas_extra = horas - horas_normales
    pago_extra = horas_extra * ( paga_hora * 2)
    total = paga_normal + paga_extra

print("\n Cálculo completado.")
print(f'\{nombre} trabajo {horas} horas, a una paga de {paga_hora} pesos por hora, horas extra {horas_extra}')
print(f'Paga normal         : ${paga_normal:13,.2f}')
print(f'Paga extra          : ${paga_extra:13,.2f}')
print(f'El pago total       : ${total:13,.2f}')
print('\n* ¡Programa finalizado! *')