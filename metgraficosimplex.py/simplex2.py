"""
   Cortadores       : [8, 28], SI NO FUERA DE RANGO
   Maquinas de Coser: [35,52], SI NO FUERA DE RANGO
   Empacadores      : [18,48], SI NO FUERA DE RANGO
"""
# desarrollo del problema en general 

from pulp import *
import pandas as pd

# Definir el problema de optimización
problema = LpProblem("Maximizar_Utilidad", LpMaximize)

# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat='Integer') #Jeans 
x2 = LpVariable("x2", lowBound=0, cat='Integer') #Franelas 
x3 = LpVariable("x3", lowBound=0, cat='Integer') #Amasados 
# Definir la función objetivo

problema += 400*x1 + 200*x2 + 300*x3, 'Z'

#Respondiendo la letra B

while True:
    try:
        
        while True:
            limite1 = int(input("Ingrese la disponibilidad nueva de Cortadores: "))

            if limite1 >= 8 and limite1 <= 28:
                break
            else:
                print("Ingrese un valor dentro del rango solicitado")

        while True:
            limite2 = int(input("Ingrese la disponibilidad nueva de Maquinas de Coser: "))

            if limite2 >= 30 and limite2 <= 52:
                break
            else:
                print("Ingrese un valor dentro del rango solicitado")

        while True:
            limite3 = int(input("Ingrese la disponibilidad nueva de Empacadores: "))

            if limite3 >= 18 and limite3 <= 48:
                break
            else:
                print("Ingrese un valor dentro del rango solicitado")
    except ValueError:
        print("Ingrese una número Valido")
        continue
    break

#cambio de restricciones en el vector de disponibilidad 

problema += 4*x1 + 2*x2 +   x3 <= limite1, "Cortadores"
problema +=   x1 + 2*x2 + 2*x3 <= limite2, "Maquinas_de_Coser" 
problema +=   x1 +   x2 +   x3 <= limite3, "Empacadores"

problema.solve()

# Imprimir el resultado
print("Estado:", LpStatus[problema.status])
print("Valor óptimo de Z:", problema.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in problema.variables():
    print(f"{var.name}: {var.value()}")

sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack} for i, j in problema.constraints.items()]

print(pd.DataFrame(sensibilidad))