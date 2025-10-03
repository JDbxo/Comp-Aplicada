# p066-primer-parcial.py
"""
Programa de ventas de boletos de un cine 
Juan Diego De Avila Velazquez
Matricula: 37186143
Materia: Computación Aplicada
Examen: Primer Parcial
"""
print('\033[H\033[J')

total_ventas = total_asist = suma_edad = 0
venta = b_negados = 0
ce = ca = ct = cu = sh = sm = 0
total_e = total_a = total_t = total_u = total_h = total_m = 0

while True:
    venta += 1
    print(f'venta {venta}: ')

    edad = int(input('Ingresa tu edad: '))
    if edad > 13:
        print('Adelante')
    else:
        print('No tienes la edad requerida')
        b_negados += 1 
        venta -= 1
        continue
        
    tipo = input('Tipo de comprador Estudiante (E) $50, Adulto (A) $90, Tercera Edad (T) $60, Academico (U) $70: ').upper()
    sexo = input('Hombre (H), Mujer (M): ').upper()
    
    if tipo not in 'EATUHM':
        err = input ('>>>>Error tipo de comprador o sexo no valido\n Intente de nuevo, <Enter>')
        boletos -= 1
        continue

    if sexo == 'H':
        sh += 1
    elif sexo == 'M':
        sm += 1
    
    total_asist += 1
    suma_edad += edad

    if tipo == 'E':
        ce += 1
        total_e =  total_e + 50
    elif tipo == 'A':
        ca += 1
        total_a = total_a + 90
    elif tipo == 'T':
        ct += 1
        total_t = total_t + 60
    elif tipo == 'U':
        cu += 1
        total_u = total_u + 70
    if tipo == 'E' and sexo == 'H':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Hombre')
        print(f'Tipo de comprador Estudiante')
    elif tipo == 'A' and sexo == 'H':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Hombre')
        print(f'Tipo de comprador Adulto')
    elif tipo == 'T' and sexo == 'H':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Hombre')
        print(f'Tipo de comprador Tercera edad')
    elif tipo == 'U' and sexo == 'H':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Hombre')
        print(f'Tipo de comprador Academico')
    elif tipo == 'E' and sexo == 'M':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Mujer')
        print(f'Tipo de comprador Estudiante')
    elif tipo == 'A' and sexo == 'M':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Mujer')
        print(f'Tipo de comprador Adulto')
    elif tipo == 'T' and sexo == 'M':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Mujer')
        print(f'Tipo de comprador Tercera edad')
    elif tipo == 'U' and sexo == 'M':
        print('\n BIENVENIDO')
        print(f'Edad: {edad}')
        print(f'Sexo: Mujer')
        print(f'Tipo de comprador Academico')

    if input('Otra venta (S/N) ?').upper() != 'S':break

total_ventas = total_e + total_a + total_t + total_u
promedio_e = suma_edad / total_asist

print('\n-------------------------')
print('Resumen de venta de boletos')
print('----------------------------')
print(f'ventas realizadas: {venta}')
print('----------------------------')
print(f'Total de Estudiantes      : {ce}')
print(f'Total de Adultos          : {ca}')
print(f'Total de Tercera Edad     : {ct}')
print(f'Total de Academicos       : {cu}')
print(f'Total de Hombres          : {sh}')
print(f'Total de Mujeres          : {sm}')
print(f'Promedio de edad de los asistentes: {promedio_e:2f}')
print(f'Personas rechazadas por edad      : {b_negados}')
print('----------------------------')
print(f'Total dinero recaudado por estudiantes \t : {total_e}')
print(f'Total dinero recaudado por adultos \t : {total_a}')
print(f'Total dinero recaudado por tercera edad : {total_t}')
print(f'Total dinero recaudado por academicos \t : {total_u}')
print(f'Total recaudado \t : {total_ventas}')

mensaje_venta=""
if total_ventas > 3500:
    mensaje_venta = "La funcion genero BUENAS ganancias"
elif total_ventas >= 1500 and total_ventas <= 3500:
    mensaje_venta="La funcion genero ganancias MODERADAS"
else:
    mensaje_venta="La funcion genero Bajas ganancias"
print('-----------------------')    
print('Rentabilidad')    
print(mensaje_venta)

print('\n Fin de las ventas por hoy')



"""
Pregunta 1: agregaria una variable previamente inicializada donde se pregunte que dia , esto antes de preguntar la edad y agregaria un if 
dentro del elif del tipo adulto (A), donde si es martes se hace la operacion de descuento con una variable de descuento: (total_a * 0.8) 
y agregaria otra variable que refleje el total del descuento realizado. 

Pregunta 2: Limito el codigo hasta los if: 
if tipo == 'E':
        ce += 1
        total_e =  total_e + 50
    elif tipo == 'A':
        ca += 1
        total_a = total_a + 90
    elif tipo == 'T':
        ct += 1
        total_t = total_t + 60
    elif tipo == 'U':
        ce += 1
        total_u = total_u + 70


y revisaria que las varibles del total esten inicializadas en cero, revisaria que la opercion sea la correcta en los if de cada tipo 
EATU, que se este sumando en realidad el precio del boleto, revisaria que las variables esten bien escritas, ademas de imprimir cada 
variable de total por separado

"""