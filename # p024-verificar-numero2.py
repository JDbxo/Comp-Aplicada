# p024-verificar-numero.py
# Verificar si un numero es positivo, negativo o cero

print('Verificar si un numero es positivo, negativo o cero')
#Entrada
numero = int(input('Dame un numero entero: '))

if numero == 0:

    print('El numero es CERO 😑 ')

else:
    if numero < 0:

        print('El numero es NEGATIVO 😒')
    
    else:
        print('El numero es numero es POSITIVO 😀')

print('\nProceso terminado')