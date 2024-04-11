def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: división por cero"

while True:
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print("El resultado de la suma es:", resultado)
        
    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = restar(num1, num2)
        print("El resultado de la resta es:", resultado)
        
    elif opcion == '3':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
        
    elif opcion == '4':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir(num1, num2)
        print("El resultado de la división es:", resultado)
        
    elif opcion == '5':
        print("Saliendo de la calculadora.")
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