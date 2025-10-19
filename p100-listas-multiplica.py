#p100-listas-multiplica.py
#Programa para multiplicar numeros de lisats 

lista_a = []
lista_b = []

print('Introduzca 5 numeros para la lista A:')
for i in range(5):
    num = int(input(f"A[{i+1}]: "))
    lista_a.append(num)

print('\nIntroduzca 5 numeros para la lista B:')
for i in range(5):
    num = int(input(f'B[{i+1}]: '))
    lista_b.append(num)

lista_c = [lista_a[i] * lista_b[i] for i in range(5)]

print('\n--- Resultados ---')
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
print(f'Lista C (A * B): {lista_c}')


