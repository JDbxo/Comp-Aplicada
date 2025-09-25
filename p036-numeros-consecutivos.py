# p036-numeros-consecutivos.py
# Determinar si tres números son consecutivos

print('Dame 3 números enteros separados por espacio:')
n1, n2, n3 = input().split()
# Convertir las entradas a enteros
n1, n2, n3 = int(n1), int(n2), int(n3)

# Verificación de consecutividad en cualquier orden
if (n2 == n1 + 1 and n3 == n2 + 1) or (n1 == n2 + 1 and n3 == n1 + 1) or (n1 == n3 + 1 and n2 == n1 + 1):
    print("Los números son consecutivos.")
else:
    print("Los números NO son consecutivos.")
