# p042-precio-entrada-cine.py
# Precio de entrada al cine según la edad

print("Taquilla Cine")
edad = int(input("Ingrese su edad: "))

if edad < 5:
    print("Entrada gratis")
elif edad <= 12:
    print("El precio de la entrada es $50")
elif edad <= 17:
    print("El precio de la entrada es $70")
elif edad <= 59:
    print("El precio de la entrada es $100")
else:
    print("El precio de la entrada es $60 (descuento para adultos mayores)")
