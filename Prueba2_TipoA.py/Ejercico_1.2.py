"""
Debido a la necesidad de ver el cambio en los rangos de los contenidos porcentuales medidos, se le 
pide a usted:

6) Hacer que el vector de recursos disponibles de las restricciones que representan el límite 
superior de los contenidos porcentuales sea variable. Programe en Python para que se pueda
ver el comportamiento de la solución óptima.
Se pide que el programa tenga:

1.Un menú básico que tenga dos opciones, siendo estas una para salir del menú y otra 
opción que permita variar el rango de los elementos medidos. (5 pts)

2.Se pide que el programa capture el error dejándote un mensaje de ayuda y te devuelva al 
menú en caso de que se digiten mal los valores. (5 pts)

3.Al ingresar a la opción “variar el rango”, el programa debe solicitar el % de variación de 
los límites superiores de las restricciones generadas, siendo en este caso el % entre 10 y 
12 por ciento y que además, al terminar el input se muestre la solución óptima del 
problema. (8 pts)

4.Se pide que el programa capture el error dentro de la opción “varíar el rango” y que en 
caso de digitar mal los valores el programa deje un mensaje de ayuda y te devuelva al 
menú. (5 pts)

7) ¿Qué opina si se hace variable los rangos?, ¿Afecta positiva o negativamente a la solución 
óptima del problema? (3 pts)

"""

from pulp import *
import pandas as pd 

def Calculo_de_Composicion_quimica():
     while True:
        try:
            while True:

                limite1 = float(input("\nIngrese la variacion de [0.1 o 0.12]: "))

                if limite1 >= 0.1 and limite1 <= 0.12:   #CREACION PROPIA [J.chaparro.S]
                    problema = LpProblem("Minimazando los costos de produccion", LpMinimize)
                    #definimos las varables del problema 
                    x1 = LpVariable("x1", lowBound=0, cat= 'Continuous')
                    x2 = LpVariable("x2", lowBound=0, cat= 'Continuous')
                    x3 = LpVariable("x3", lowBound=0, cat= 'Continuous')
                    x4 = LpVariable("x4", lowBound=0, cat= 'Continuous')
                    x5 = LpVariable("x5", lowBound=0, cat= 'Continuous') 
                    
                    #Funcion objetivo 

                    problema += 450*x1 + 400*x2 + 500*x3 + 600*x4 + 400*x5

                    #Definimos las trestricciones 

                        #Limites superiores 
                    problema += 10*x1 +  8*x2 + 12*x3 + 10*x4 + 15*x5 <= 10 + 10* limite1  , "NARANJA_SUP" 
                    problema += 12*x1 + 15*x2 + 12*x3 + 10*x4 +  6*x5 <= 12 + 12* limite1  , "PLATANO_SUP"
                    problema +=  8*x1 + 11*x2 +  7*x3 + 10*x4 + 10*x5 <=  8 +  8* limite1  , "LECHE_SUP"
                    problema +=  5*x1 +  2*x2 +  7*x3 +  5*x4 + 10*x5 <=  5 +  5* limite1  , "ADITIVOS_SUP"

                        #Limites inferiores 
                    problema += 10*x1 +  8*x2 + 12*x3 + 10*x4 + 15*x5 >= 10 , "NARANJA_INF" #Se mantiene con los originales 
                    problema += 12*x1 + 15*x2 + 12*x3 + 10*x4 +  6*x5 >= 12 , "PLATANO_INF"
                    problema +=  8*x1 + 11*x2 +  7*x3 + 10*x4 + 10*x5 >= 8  , "LECHE_INF"
                    problema +=  5*x1 +  2*x2 +  7*x3 +  5*x4 + 10*x5 >= 5  , "ADITIVOS_INF"

                        # Restricción de que la suma de las proporciones debe ser 1 (100%)
                    problema += x1 + x2 + x3 + x4 + x5 == 1, "SUMA_PROPORCIONES"

                        #Se resuelve el problema
                    problema.solve()

                        # Imprimir el resultado
                    print("\nEstado:", LpStatus[problema.status])

                    print("\nCosto total de Produccion:", problema.objective.value())

                    print("\nValores óptimos de x1, x2, x3, x4, x5:")
                    for var in problema.variables():
                        print(f"{var.name}: {var.value()}")

                        print()

                    sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack} for i, j in problema.constraints.items()]
                    print(pd.DataFrame(sensibilidad))
                    break
                else:
                    print("Ingrese un valor dentro del rango solicitado")               
        except ValueError:
            print("Error, ingrese un número Valido")
            continue
        break            
       
        
    

def main():
    while True:
        try:
            #Creamos el menu de entrada que permitira mostrar las opciones al usuario
            print(""" 
                ======= Menu de Calculo de Composicion Quimica =======
                1. Calcular Composicion.
                2. Salir.
                """)
                       
            opcion= int(input("Ingrese una opción: "))
            
            if opcion == 1:
                Calculo_de_Composicion_quimica()     
                
            elif opcion == 2:
                print("Gracias por trabajar con nosotros")
                print("Saliendo del Programa...")
                break
            else:
                print("Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("Error. Ingrese opcion valida.")

if __name__ == '__main__':
    main()

