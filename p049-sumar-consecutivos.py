# p049-sumar-consecutivos.py
# Suma números hasta que el total sea >= 100.
c = 0
suma = 0
meta = 5000
print(" Meta de ahorro: $100. Empezando a sumar números...")
# El ciclo está programado para correr hasta 200, pero el 'break' lo detendrá antes.
while c < 200:
    c += 1
    suma += c
    print(f" (+{c})", end="")
    
    if suma >= meta:
        print("\n\n ¡Meta alcanzada!")
        print(f'Boletos{c}')
        # La palabra 'break' termina el ciclo INMEDIATAMENTE.
    break

print(f"Se necesitaron los primeros {c} números para llegar a una suma de ${suma}.")