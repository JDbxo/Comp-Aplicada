# p022-resistencia-equivalente-paralelo
# Calcular la resistencia equivalente de 4 resistencias en paralelo

print('Ingrese el valor de la resistencia R1')
r1 = float(input())
print('Ingrese el valor de la resistencia R2')
r2 = float(input())
print('Ingrese el valor de la resistencia R3')
r3 = float(input())
print('Ingrese el valor de la resistencia R4')
r4 = float(input())

rt = 1 / ((1/r1) + (1/r2) + (1/r3) + (1/r4))

print(f"La resistencia total  del circuito es: {rt:.2f} ohmios")