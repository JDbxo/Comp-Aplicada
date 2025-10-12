# p085-rombo-caracter.py
# Dibuja un rombo con el caracter elegido por el usuario

n = int(input("Dame un numero impar para la altura: "))
while n % 2 == 0:
    print("El numero debe ser impar.")
    n = int(input("Dame un numero impar para la altura: "))

caracter = input("¿Que caracter quieres usar? ")

for i in range(1, n + 1, 2):  # solo numeros impares
    espacios = (n - i) // 2
    print(" " * espacios + caracter * i)

for i in range(n - 2, 0, -2):  # va de n-2 hasta 1
    espacios = (n - i) // 2
    print(" " * espacios + caracter * i)
