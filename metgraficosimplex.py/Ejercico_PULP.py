from pulp import * 

#Defenimos el problema de programacion lineal 

problema = LpProblem("Problema_Optimizacio_PL", LpMaximize)
#Ingresamos las variables que entraran en el sistema, ya sea X1, X2, tec.

x1 = LpVariable("X1", lowBound=0 , cat= 'Integer')
x2 = LpVariable("X2", lowBound=0 , cat= 'Integer')
""" 
Se inicia definiendo el problema con LpProblem como funcion de Pulp
LpMaximize es la funcion que se utiliza en pulp
para el caso de minimizacion en el modulo de PULP es cambiar el mx por el in "LpMimize"

LpVariable es una funcion del pulp para definir una varable 
lowBound, tambien es una funcion de pulp que permite ingresar la no negatividad del problem 
cat, otra funcion que nos permite ...
itenger ...
"""

#se define la Funcion Objetivo 

problema += 2*x1-4*x2

# Restriccion S.a

problema += -x1  +  x2 <=3
problema += -x1  +2*x2 >=-3
problema += 3*x1 +  x2 == 3

#Ahora desarrollamos el solver para ejecutarlo 

problema.solve()

print("")
print("El optimo se obtiene con x1= ", x1.varValue, "y x2= ",x2.varValue)


