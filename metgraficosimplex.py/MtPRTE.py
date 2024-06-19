from pulp import *


# Creamos el Problemao principal, indicando el sentido de la función objetivo
Problema = LpProblem("Problema de transporte", LpMinimize)

# Definimos las variables decisión y su conjunto (Ej:Continuos, Integer)
x11 = LpVariable("x11", lowBound=0, cat='Integer')
x12 = LpVariable("x12", lowBound=0, cat='Integer')
x21 = LpVariable("x21", lowBound=0, cat='Integer')
x22 = LpVariable("x22", lowBound=0, cat='Integer')
x31 = LpVariable("x31", lowBound=0, cat='Integer')
x32 = LpVariable("x32", lowBound=0, cat='Integer')


#Definimos la funcion objetivo

# Definimos la función objetivo
Problema += 8*x11 + 6*x12 + 9*x21 + 12*x22 + 14*x31 + 9*x32

# Definimos las restricciones del problema asociado
#ESTAS SON LAS OFERTAS
Problema += x11 + x21 + x31 == 20, "R1"
Problema += x12 + x22 + x32 == 30, "R2"


#ESTAS SON LAS DEMANDAS
Problema += x11 + x12  == 15, "R3"
Problema += x21 + x22  == 25, "R4"
Problema += x31 + x32  == 10, "R5"


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
