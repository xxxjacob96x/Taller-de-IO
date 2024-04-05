# Inicio del programa
#### """tengo que mejorar el proceso para que retorne al MENU!!!"""#########

while True:
    print("\n=====Menu====")
    print("calcular (1)")
    print("Salir (2)")


    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
     
        A = float(input("Ingrese valor de base del rectangulo y triangulo: "))
        B = float(input("Ingrese el valor de B: "))
        C = float(input("Ingrese el valor de C: "))
        AT = (B * (A - C)) / 2
        AR = B * C 
        
        Area = AT + AR
    
        if C < A:

            print("El área es:", Area, "Mts^2")

        else:
            print("A ES MENOR QUE C ")
            print("Seleccione una opcion")
            continue
        
    elif opcion =='2':
        print("Saliendo de la calculadora.")
        break



# Fin del programa
