# p008-entrada-con-espacio.py
# Leer tres números enteros con espacio

print('Entrada de varios valores separados por un espacio :')

print('\nDame tres números, separados por un espacio :')

n1, n2, n3 = input().split()#lee una linea y la separa en base al espacio (split)

n1, n2, n3 = [ int(n1), int(n2), int(n3) ]

print('Los valores introducidos son:')

print(n1, n2, n3)