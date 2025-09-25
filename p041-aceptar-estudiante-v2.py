# p041-aceptar-estudiante-v2
# Evaluación de ingreso a Universidad Kitty Kat SA

print("Proceso de admisión")

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (h/m): ").lower()
edad = int(input("Ingrese su edad: "))

print("\nIngrese sus 3 calificaciones:")
c1 = float(input("Calificación 1: "))
c2 = float(input("Calificación 2: "))
c3 = float(input("Calificación 3: "))

# promedio
promedio = (c1 + c2 + c3) / 3

print(f"\nResultado para {nombre}:")
if sexo != "m":
    print("Rechazado: la universidad solo acepta mujeres")
elif edad <= 21:
    print("Rechazado: debe ser mayor de 21 años")
elif promedio < 8 or promedio > 9.5:
    print(f"Rechazado: el promedio {promedio:.2f} no está en el rango permitido")
else:
    print(f"Aceptada: ¡Felicidades {nombre}! Cumples con todos los requisitos")
