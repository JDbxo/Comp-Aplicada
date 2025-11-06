# p125-segundo-examen-parcial.py
"""
Programa de gestion de un inventario
Juan Diego De Avila Velazquez
Matricula: 37186143
Materia: Computación Aplicada
Examen: Segundo Parcial
"""
print('\033[H\033[J')

inventario = [] #Lista para almacenar los productos

print("Ingresa los datos de los productos. Escriba 'fin' para terminar.\n")

while True:
    nombre = input('Nombre del producto: ')
    # Si se escribe fin, se detiene la carga de productos
    if nombre.lower() == 'fin':
        break
    try: #Valida que el precio sea numerico
        precio = float(input('Precio: '))
    except ValueError:
        print('Error: Debe ingresar un numero valido para el precio.')
        continue 

    categoria = input("Categoria: ")
    proveedor = input("Proveedor: ")

    try:# Valida que el stock sea un numero entero
        stock = int(input("Disponible: "))
    except ValueError:
        print("Error: Debe ingresar un numero entero para el stock.")
        continue

    # Diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": stock
    }
    #Agrega el producto al inventario
    inventario.append(producto)

print('\n=== Datos ===')
print(inventario)

print('\n=== Tabla de datos ===')
print(f"{'NOMBRE':20} {'PRECIO':>10} {'CATEGORIA':15} {'PROVEEDOR':15} {'STOCK':>10}")
print("-" * 75)

for p in inventario:
    print(f"{p['nombre']:20} {p['precio']:10.2f} {p['categoria']:15} {p['proveedor']:15} {p['stock']:10}")

print('\n=== Resumen ===')

total_productos = len(inventario)

#Contar productos por categoria
categorias = {}
for p in inventario:
    cat = p["categoria"].lower()
    categorias[cat] = categorias.get(cat, 0) + 1

#Contar por proveedor
proveedores = {}
for p in inventario:
    prov = p["proveedor"].lower()
    proveedores[prov] = proveedores.get(prov, 0) + 1

# Totales y promedios de stock y precios
stocks = []
for p in inventario:
    stocks.append(p["stock"])

precios = []
for p in inventario:
    precios.append(p["precio"])

suma_stock = sum(stocks)
prom_stock = sum(stocks) / total_productos

suma_precios = sum(precios)
prom_precios = sum(precios) / total_productos

#Determinar el producto mas caro y mas barato
precio_max = max(precios)
precio_min = min(precios)
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)
producto_mas_caro = inventario[pos_max]
producto_mas_barato = inventario[pos_min]

print(f"Total de productos registrados: {total_productos}")
print("\nProductos por categoría:")
print(f"Laptops: {categorias.get('laptops', 0)}")
print(f"Celulares: {categorias.get('celulares', 0)}")
print(f"Audio: {categorias.get('audio', 0)}")
print(f"Accesorios: {categorias.get('accesorios', 0)}")

print("\nProductos por proveedor:")
print(f"HP: {proveedores.get('hp', 0)}")
print(f"Lenovo: {proveedores.get('lenovo', 0)}")
print(f"Apple: {proveedores.get('apple', 0)}")
print(f"Samsung: {proveedores.get('samsung', 0)}")
print(f"Sony: {proveedores.get('sony', 0)}")
print(f"Generico: {proveedores.get('generico', 0)}")


print(f"\nSuma total del stock: {suma_stock}")
print(f"Promedio de stock: {prom_stock:.2f}")
print(f"Suma total de precios: ${suma_precios:.2f}")
print(f"Promedio de precios: ${prom_precios:.2f}")

print(f"\nEl producto más caro es '{producto_mas_caro['nombre']}' con un precio de ${precio_max:.2f}.")
print(f"El producto más barato es '{producto_mas_barato['nombre']}' con un precio de ${precio_min:.2f}.")