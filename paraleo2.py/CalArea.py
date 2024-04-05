# Ingreso de la informacion 

while True:

    print(""" 
        \n======Menu Calculo de Area ======
          1. Calcular Area.
          2. Salir

        """)
    
    opcion= input("Selecciones una Opcion: ")

    if opcion == '1':

        A = float(input("Altura del triangulo rectangulo y rectangulo unido /(A): "))
        B = float(input("Base del trisngulo y del rectangulo /(B): "))
        C = float(input("Altura del Rectangulo /(C): "))

        #Calculo de Proceso 
        AT = (B * (A - C)) / 2
        AR = B * C 

        Area = AT + AR

        
        if C < A:
            print("El area de la figura es: ", Area)
            
        else: 
            print("A es mayor que C")
            print("Vuelva a intentarlo")
            continue

    elif opcion == '2': 
        print("Saliendo.....")
        break

    