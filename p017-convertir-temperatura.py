# p017-convertir-temperatura
# Convertir temperatura de grados celsius a grados fahrenheit

print('Conversor de Celsius a Fahrenheit')
print('Dame la temperatura en celsius')
cel = float(input())

fa = (cel * (9/5)) + 32

print(f'La temperatura de {cel:.1f}° C equivale a {fa:.1f} Fahrenheit')