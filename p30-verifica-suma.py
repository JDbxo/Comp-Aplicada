# p30-verifica-suma.py
# Verificar si la suma de dos números es igual a un tercero.

print('\033[2J\033[H')
print('Verificar si la suma de dos números es igual a un tercero')

print('Dame 3 números enteros separados por espacio:')
n1, n2, n3 = input().split()
# Convertir las entradas a enteros
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
    print(f' {n1} + {n2} = {n3} ')
elif n1 + n3 == n2:
        print(f' {n1} + {n3} = {n2} ')
elif n2 + n3 == n1:
    print(f' {n2} + {n3} = {n1} ')
elif n1 == n2 == n3:
    print(f' {n1} , {n2} , {n3}, son iguales ')
elif n1 != n2 != n3:
    print(f' {n1} , {n2} , {n3}, son diferentes ')
else:
# Si ninguna de las condiciones anteriores se cumple
    print(f' Es probable que {n1} , {n2} , {n3} sea un par igual.')