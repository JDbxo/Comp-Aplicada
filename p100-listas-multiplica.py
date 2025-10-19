#p100-listas-multiplica.py
#Programa para multiplicar numeros de lisats 

lista_a = []
lista_b = []

lista_a = list(map(int, input('Introduzca 5 numeros para la lista A: ').split()))

while len(lista_a) != 5:
    print('Debe introducir exactamente 5 numeros.')
    lista_a = list(map(int, input('Introduzca 5 numeros para la lista A: ').split()))

lista_b = list(map(int, input('Introduzca 5 numeros para la lista B: ').split()))

while len(lista_b) != 5:
    print('Debe introducir exactamente 5 numeros.')
    lista_b = list(map(int, input('Introduzca 5 números para la lista B: ').split()))

lista_c = [lista_a[i] * lista_b[i] for i in range(5)]

print('\n--- Resultados ---')
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
print(f'Lista C (A * B): {lista_c}')

