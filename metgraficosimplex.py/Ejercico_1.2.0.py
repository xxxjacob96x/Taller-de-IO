from pulp import *
import pandas as pd

def input_within_range(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Ingrese un valor dentro del rango solicitado ({low}-{high})")
        except ValueError:
            print("Error, ingrese un número válido")

def Calculo_de_Composicion_quimica():
    problema = LpProblem("Minimizando_los_costos_de_produccion", LpMinimize)

    # Definimos las variables del problema
    x1 = LpVariable("x1", lowBound=0, cat='Continuous')
    x2 = LpVariable("x2", lowBound=0, cat='Continuous')
    x3 = LpVariable("x3", lowBound=0, cat='Continuous')
    x4 = LpVariable("x4", lowBound=0, cat='Continuous')
    x5 = LpVariable("x5", lowBound=0, cat='Continuous')

    # Función objetivo
    problema += 450*x1 + 400*x2 + 500*x3 + 600*x4 + 400*x5

    # Obtener los límites de disponibilidad
    limite1 = input_within_range("Ingrese la disponibilidad nueva de Naranja_SUP: ", 10, 12)
    limite1_1 = input_within_range("Ingrese la disponibilidad nueva de Naranja_INF: ", 10, 12)
    limite2 = input_within_range("Ingrese la disponibilidad nueva de Plantano_SUP: ", 10, 12)
    limite2_2 = input_within_range("Ingrese la disponibilidad nueva de Plantano_INF: ", 10, 12)
    limite3 = input_within_range("Ingrese la disponibilidad nueva de LECHE_SUP: ", 10, 12)
    limite3_3 = input_within_range("Ingrese la disponibilidad nueva de LECHE_INF: ", 10, 12)
    limite4 = input_within_range("Ingrese la disponibilidad nueva de Aditivos_SUP: ", 10, 12)
    limite4_4 = input_within_range("Ingrese la disponibilidad nueva de Aditivos_INF: ", 10, 12)

    # Definimos las restricciones
    problema += 10*x1 + 8*x2 + 12*x3 + 10*x4 + 15*x5 <= limite1, "NARANJA_SUP"
    problema += 12*x1 + 15*x2 + 12*x3 + 10*x4 + 6*x5 <= limite2, "PLATANO_SUP"
    problema += 8*x1 + 11*x2 + 7*x3 + 10*x4 + 10*x5 <= limite3, "LECHE_SUP"
    problema += 5*x1 + 2*x2 + 7*x3 + 5*x4 + 10*x5 <= limite4, "ADITIVOS_SUP"

    problema += 10*x1 + 8*x2 + 12*x3 + 10*x4 + 15*x5 >= limite1_1, "NARANJA_INF"
    problema += 12*x1 + 15*x2 + 12*x3 + 10*x4 + 6*x5 >= limite2_2, "PLATANO_INF"
    problema += 8*x1 + 11*x2 + 7*x3 + 10*x4 + 10*x5 >= limite3_3, "LECHE_INF"
    problema += 5*x1 + 2*x2 + 7*x3 + 5*x4 + 10*x5 >= limite4_4, "ADITIVOS_INF"

    # Restricción de que la suma de las proporciones debe ser 1 (100%)
    problema += x1 + x2 + x3 + x4 + x5 == 1, "SUMA_PROPORCIONES"

    # Resolver el problema
    problema.solve()

    # Imprimir el resultado
    print("\nEstado:", LpStatus[problema.status])
    print("\nCosto total de Produccion:", value(problema.objective))
    print("\nValores óptimos de x1, x2, x3, x4, x5:")
    for var in problema.variables():
        print(f"{var.name}: {var.value()}")

    print()
    sensibilidad = [{'Restricción ': i, 'Precio Sombra': j.pi, 'Holgura': j.slack} for i, j in problema.constraints.items()]
    print(pd.DataFrame(sensibilidad))

def main():
    while True:
        try:
            print(""" 
                ======= Menu de Calculo de Composicion Quimica =======
                1. Calcular Composicion.
                2. Salir.
                """)
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                Calculo_de_Composicion_quimica()
            elif opcion == 2:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Error. Ingrese opción válida.")

if __name__ == '__main__':
    main()
