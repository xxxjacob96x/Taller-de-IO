#Todo problema tiene un inicio, proceso y Fin
#Entonces

#Inicio
def calculo_ganacia():
    while True:
        try:
            L = float(input("Ingrese la cantidad de litros producidos: "))##Tipo entero
            if L < 0:
                print("Error: Ingrese un numero positivo.")
                continue
            PG = float(input("Precio del Galon: ")) #tipo real 
            if PG < 0:
                print("Ingrese un valor positivo.")
                continue
            break# si llegamos a este puento, significa que los valores fueron validados
        except ValueError:
            print("Error: Por favor, ingrese un numero valido.")

    #Proceso Interno
    cant_galon_producido = L / 3.785
    ganacia = cant_galon_producido * PG
    #Este vendria siendo el ouput 
    print("\nLa ganacia es:$", round(ganacia,))

def main():
    while True:
        try: 

            print("""\n
            ====== Menu Calculo de Ganancias =====
                1.Calcular Ganancia.
                2. Salir 

                """)
            
            opcion = int(input("\nSeleccione una Opcion: "))

            if opcion == 1:
                calculo_ganacia()
            elif opcion == 2:
                print("Saliendo....")
                break
            else:
                print("Opcion no valida. Elija 1 o 2: ")
                continue
        except ValueError:
            print("Error, vuelva a intentar ")

if __name__ == '__main__':
    main()





