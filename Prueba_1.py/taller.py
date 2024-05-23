"""
Crear un programa para gestionar el inventario de una pequeña tienda. 
El programa debe permitir agregar, actualizar, eliminar y visualizar productos en el inventario. 
Cada producto tiene un nombre, un código, una cantidad y un precio.

Requisitos:
Agregar un producto:

Solicitar al usuario el nombre, el código, la cantidad y el precio del producto.
===>Asegurarse de que el código del producto sea único.
Actualizar un producto:

Permitir al usuario actualizar la cantidad y el precio de un producto existente basado en su código.
Eliminar un producto:

Permitir al usuario eliminar un producto del inventario basado en su código.
Visualizar el inventario:

Mostrar todos los productos en el inventario con su nombre, código, cantidad y precio.
Menu principal:

El programa debe mostrar un menú principal que permita al usuario seleccionar una de las opciones anteriores.

"""
# Sistema de Gestión de Inventario
inventario = []

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    if codigo in inventario:
        print("Error: Ya existe un producto con ese código.")
        return
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    inventario[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    print("Producto agregado exitosamente.")

def actualizar_producto():
    codigo = input("Ingrese el código del producto a actualizar: ")
    if codigo not in inventario:
        print("Error: No existe un producto con ese código.")
        return
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    precio = float(input("Ingrese el nuevo precio del producto: "))
    inventario[codigo]["cantidad"] = cantidad
    inventario[codigo]["precio"] = precio
    print("Producto actualizado exitosamente.")

def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo not in inventario:
        print("Error: No existe un producto con ese código.")
        return
    del inventario[codigo]
    print("Producto eliminado exitosamente.")

def visualizar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    for codigo, datos in inventario.items():
        print(f"Código: {codigo}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")

def menu_principal():
    inventario = {}
    while True:
        print( "\n=== Menú Principal ===="
              "1. Agregar Producto"
              "2. Actualizar Producto"
              "3. Eliminar Producto"
              "4. Visualizar Inventario"
              "5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            actualizar_producto(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            visualizar_inventario(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
