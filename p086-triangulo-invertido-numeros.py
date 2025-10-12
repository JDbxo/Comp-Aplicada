# p086-triangulo-invertido-numeros.py
# Imprime un triangulo numerico invertido

n = int(input("Dame un numero: "))

for i in range(n, 0, -1):      
    for j in range(1, i + 1):  
        print(j, end=" ")
    print()
