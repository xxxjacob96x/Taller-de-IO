def sumar():
    return num1 + num2

def restar():
    return num1 - num2

def multiplicar():
    return num1 * num2

while True:
    print("\nCalculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar()
        print("\n El resultado de la división es:", resultado)

        
    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = restar()
        print("\n El resultado de la división es:", resultado)

        
    elif opcion == '3':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicar()
        print("\n El resultado de la división es:", resultado)

        
    elif opcion == '4':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
         resultado = num1 / num2
        else:
            print("Error: división por cero")
        print("\n El resultado de la división es:", resultado)
        
    elif opcion == '5':
        print("\n Saliendo de la calculadora.")
        break
        
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

"""
Crea un programa en Python que simule una calculadora simple con las operaciones de suma y resta. 
El programa debe mostrar un menú con las siguientes opciones:

Sumar
Restar
Salir
El programa debe permitir al usuario seleccionar una de estas opciones ingresando el número correspondiente. 
Si elige sumar o restar, se le pedirá ingresar dos números y se mostrará el resultado de la operación seleccionada. 
Si elige salir, el programa terminará.

"""

""" 



"""