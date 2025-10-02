"""""
p065-sistemapapeleria.py
Programa para calcular las ventas de una papeleria
Autor: Juan Diego De Avila Velazquez
# Fecha: 2/10/2025
"""""
print('\033[H\033[J')

ventas = cantidad = subtotal = 0
total_c = total_o = total_d = total_p = 0

cantidad_o = cantidad_c = cantidad_d = cantidad_p = 0
total_o = total_c = total_d = total_p = 0

while True:
    ventas += 1
    print(f'\nVenta {ventas}')

    tipo = input('Tipo de copia (C) carta $3, (O)oficio $4,(D) doble $6, (P)plano $12 ?').upper()

    if tipo not in 'CODP':
        err = input ('>>>>Error tipo de copia no valido inente de nuevo, <Enter>')
        ventas -= 1
        continue
    
    cantidad = int(input('Cantidad ?'))
    descuento = 1 
    if cantidad > 50:
        descuento = 0.90 # El complemento de 10%
        print('** Descuento del 10% aplicado por volumen de venta **')

    if tipo == 'C':
        cantidad_c += cantidad
        subtotal = (cantidad *3) * descuento
        total_c += subtotal
    elif tipo == 'O':
        cantidad_o += cantidad
        subtotal = (cantidad *4) * descuento
        total_o += subtotal
    elif tipo == 'D':
        cantidad_d += cantidad
        subtotal = (cantidad *6) * descuento
        total_d += subtotal
    elif tipo == 'P':
        cantidad_p += cantidad
        subtotal = (cantidad *12) * descuento
        total_p += subtotal

    if input('Otra venta (S/N) ?').upper() != 'S':break

total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p
total_ventas = total_c + total_o + total_d + total_p

print('\n-------------------------')
print('Resumen diario de ventas')
print('----------------------------')
print(f'ventas realizadas: {ventas}')
print('----------------------------')
print(f'Carta\t\t      : {cantidad_c:2d} - $ {total_c:8.3f}')
print(f'Oficio\t\t      : {cantidad_o:2d} - $ {total_o:8.3f}')
print(f'DobleOficio\t     : {cantidad_d:2d} - $ {total_d:8.3f}')
print(f'Plano\t\t      : {cantidad_p:2d} - $ {total_p:8.3f}')
print('----------------------------')
print(f'Total ventas\t : {total_copias:2d} - $ {total_ventas:8.3f}')

mensaje_venta=""
if total_ventas > 150:
    mensaje_venta = "Venta Superada"
elif total_ventas >= 50:
    mensaje_venta="Venta Frecuente"
else:
    mensaje_venta="Venta Moderada"
print(f'Esta venta es una: {mensaje_venta}')

print('\n Fin de las ventas por hoy')
