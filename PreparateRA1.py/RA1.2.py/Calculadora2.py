#ustede puede comentarios dentro de las lineas de codigo 

"""utedes puende tener un la liena de codigo y la quieren convertir a texto"""

#hay que conocer lo siguiente 

"""print("Y puede ponner un texto") """#"""==> esto conocemos como los ouput de informacion """

#cuando le habelen de ingresar nombre 
# entradas == procesos ==== y salidas 



#===============
"""Estructuras de datos con listas"""

#Base de Datos, pero que es una lista, literalmente 

Nombres =[]

def ingreso_Nombre():
     while True:

        nombre = str(input("Ingrese el nombre: ")) # input (entraDA DE INFORMACION)
        if nombre == 'salir':
            break
        Nombres.append(nombre)
            
def Mostrar_Nombres():
    print("\n === Lista de Nombres ===")

    for nombre in Nombres:
        
        print(nombre)

def main():
    while True:

        print("""
              \n======== Menu =========
            opcion 1: ingresar Nombres.
            opcion 2: Mostrar Nombres.
            opcion 3: Salir (push N°3).
              """)
        
        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            ingreso_Nombre()

        elif opcion == '2' :
            Mostrar_Nombres()

        elif opcion == '3':

            print("Saliendo.....")
            return
        
        else:
            print("Opcion invalida, Intente Nuevamente.")
if __name__ == "__main__":
    main()