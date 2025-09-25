# p051-adivina-numero.py
# Permitir que el usuario realice múltiples intentos hasta que encuentre la respuesta correcta

import random

print('033[2J\033[H')
print(" ¡Bienvenido al juego 'Adivina el Número'! ")
print("Yo te doy un numero entre 1 y 50. ¿Podrás adivinarlo?")

numero_secreto = random.randint(1, 50) # Se elige un numero entero al azar entre 1 y 50.
intento_usuario = 0
contador_intentos = 0

while True:
    intento_usuario = int(input("Tu numero: "))
    contador_intentos += 1
    
    if intento_usuario < numero_secreto:
        print(" ¡Demasiado bajo! Intenta con un numero más alto.")
    elif intento_usuario > numero_secreto:
        print(" ¡Demasiado alto! Intenta con un numero más bajo.")
    else:
        print(f"\n ¡Felicidades! ¡Adivinaste el numero secreto que era {numero_secreto}!")
        print(f"Lo lograste en {contador_intentos} intentos.")
    # Usamos 'break' para terminar el juego.
    break