# p083-plan-ahorro-depositos-mensuales.py
# Simula un plan de ahorro mensual

print('Monto inicial de ahorro:', end=' ')
monto_inicial = float(input())
print('Deposito mensual:', end=' ')
deposito = float(input())
print('Tasa de interes mensual (%):', end=' ')
tasa = float(input())
print('Numero de meses a simular:', end=' ')
meses = int(input())

print('\n    Plan de Ahorro Detallado    ')

saldo = monto_inicial

for mes in range(1, meses + 1):
    interes = saldo * (tasa / 100)
    saldo_final = saldo + interes + deposito
    print(f'Mes {mes}: Saldo Inicial: ${saldo:7.2f} | Interes: ${interes:5.2f} | Saldo Final: ${saldo_final:7.2f}')
    saldo = saldo_final

print(f'\nAl final de {meses} meses, tendras ${saldo:.2f}')
