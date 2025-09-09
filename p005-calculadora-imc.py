# p005-calculadora-imc.py
# Calcular el IMC de una persona

print("Calculadora de Índice de Masa Corporal (IMC) \n")

# Entrada
peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))

# Proceso
imc = peso_kg / (altura_m ** 2) #Divide el peso entre la altura ala cuadrado(** eleva a la potencia)

# Salida
print(f"\nTu IMC es: {imc:.2f}")

print ("\nEl peso es {0:.2f}kg y la altura es {1:.2f}m y resulta en imc de {2:.2f}".format(peso_kg,altura_m, imc))

print ("El peso es {peso_kg:.2f}kg y la altura es {altura_m:.2f}m y resulta en imc de {imc:.2f}")