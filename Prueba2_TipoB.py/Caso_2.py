"""
Melbarck LTDA (distribuidora de alimentos) presenta un problema en el departamento de logística, 
esto debido a que no se sabe cómo realizar la mejor asignación de entrega de sus productos a sus distintos clientes. 
Es por esto que se le ha encargado a usted (como Ing. Industrial) que pueda dar la mejor solución al mínimo costo.
Planteamiento del problema
La empresa cuenta con 5 centros de distribución ubicados alrededor de toda la región y tiene 5 potenciales clientes 
a los cuales ofertar sus productos, estos demandan ciertas cantidades durante el mes. Los costos para distribuir sus 
productos a sus distintos clientes dependiendo del origen va de acuerdo a lo siguiente:

         | CLIENTE 1  | CLIENTE 2   | CLIENTE 3     | CLEINTE 4     | DISPONIBILIDAD |
CENTRO 1 |      4     |     1       |      5        |       1       |       50       |
CENTRO 2 |      2     |     2       |      6        |       5       |       25       |
CENTRO 3 |      5     |     1       |      4        |       1       |       15       |
CENTRO 4 |      7     |     8       |      10       |       2       |       30       |
DEMANDAS |      20    |     45      |      25       |       30      | 


"""

## Importamos pulp para armar el modelo de programación lineal
## Importamos pandas para crear un dataframe que cálcule el análisis de sensibilidad
from pulp import *
#import pandas as pd

# Creamos el modelo principal, indicando el sentido de la función objetivo
Problema = LpProblem("Problema de transporte", LpMinimize)

# Definimos las variables decisión y su conjunto (Ej:Continuos, Integer)
x11 = LpVariable("x11", lowBound=0, cat='Integer')
x12 = LpVariable("x12", lowBound=0, cat='Integer')
x13 = LpVariable("x13", lowBound=0, cat='Integer')
x14 = LpVariable("x14", lowBound=0, cat='Integer')

x21 = LpVariable("x21", lowBound=0, cat='Integer')
x22 = LpVariable("x22", lowBound=0, cat='Integer')
x23 = LpVariable("x23", lowBound=0, cat='Integer')
x24 = LpVariable("x24", lowBound=0, cat='Integer')

x31 = LpVariable("x31", lowBound=0, cat='Integer')
x32 = LpVariable("x32", lowBound=0, cat='Integer')
x33 = LpVariable("x33", lowBound=0, cat='Integer')
x34 = LpVariable("x34", lowBound=0, cat='Integer')

x41 = LpVariable("x41", lowBound=0, cat='Integer')
x42 = LpVariable("x42", lowBound=0, cat='Integer')
x43 = LpVariable("x43", lowBound=0, cat='Integer')
x44 = LpVariable("x44", lowBound=0, cat='Integer')





# Definimos la función objetivo
Problema += 4*x11 + 1*x12 + 5*x13 + 1*x14 + 2*x21 + 2*x22 + 6*x23 + 5*x24 + 5*x31 + 1*x32 + 4*x33 + 1*x34 + 7*x41 + 8*x42 + 10*x43 + 2*x44 

# Definimos las restricciones del problema asociado
#ESTAS SON LAS demmandas
Problema += x11 + x12 + x13 + x14 == 50, "R1"
Problema += x21 + x22 + x23 + x24 == 25, "R2"
Problema += x31 + x32 + x33 + x34 == 15, "R3"
Problema += x41 + x42 + x43 + x44 == 30, "R4"


#ESTAS SON LAS disponibilidades
Problema += x11 + x21 + x31 + x41 == 20, "R7"
Problema += x12 + x22 + x32 + x42 == 45, "R8"
Problema += x13 + x23 + x33 + x43 == 25, "R9"
Problema += x14 + x24 + x34 + x44 == 30, "R10"


# Resolvemos el problema
Problema.solve()

# Imprimimos el estado final
print("Status o Estado final:", LpStatus[Problema.status])

# Imprimimos el valor de la función objetivo
print()
print("Valor de la función objetivo (Costo final) =", value(Problema.objective))
print()

# Imprimimos el valor de las variables
print("Valor de las variables: ")

for variable in Problema.variables():
    print(f"Variable {variable} = {variable.value()}")

"""

Interpretación 

1) Los valores con resultados enteros son las entregas a los clientes desde los distintos centros de distribución

"""
