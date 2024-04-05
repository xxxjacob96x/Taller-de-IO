def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

while True:
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print("El resultado de la suma es: ", resultado)
        
    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = restar(num1, num2)
        print("El resultado de la resta es: ", resultado)
        
    elif opcion == '3':
        print("Saliendo de la calculadora.")
        break
        
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
