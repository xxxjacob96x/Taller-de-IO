from pulp import *
import pandas as pd #crear data frame, para crear una tabla

problema = LpProblem("Maximizar_ Ganancias", LpMaximize)

#definimos las variales de decision, 
x1= LpVariable("x1", lowBound=0, cat= LpInteger) #PRODUCTO A
x2= LpVariable("x2", lowBound=0, cat= LpInteger) #PRODUCTO B

#DEFINIMOS AHORA LA FUNCION OBJETIVO

problema += 20000*x1 + 40000*x2, "Z"
#punto E
while True:
    limite1 = int(input("Ingrese la disponibilidad nueva de A: "))

    if limite1 >= 80 and limite1 <= 150:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

while True:
    limite2 = int(input("Ingrese la disponibilidad nueva de B: "))

    if limite2 >= 20 and limite2 <= 80:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

while True:
    limite3 = int(input("Ingrese la disponibilidad nueva de C: "))

    if limite3 >= 40 and limite3 <= 100:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

while True:
    limite4 = int(input("Ingrese la disponibilidad nueva de D: "))

    if limite4 >= 150 and limite4 <= 250:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

# Definimos las restricciones del problema asociado

problema += 4*x1 +10*x2 <= limite1 
problema += 0.5*x1 +0.8*x2 <= limite2
problema += 6*x1 +8*x2 <= limite3
problema += 8*x1 +12*x2 <= limite4 

# Resolvemos el problema
problema.solve()

# Imprimimos el estado final
print("Status o Estado final:", LpStatus[problema.status])

# Imprimimos el valor de las variables
print("Valor a producir del producto A =", value(x1))
print("Valor a producir del producto B =", value(x2))


# Imprimimos el valor de la función objetivo
print("Valor de la función objetivo (Costo final) =", value(problema.objective))
print()
sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack}
               for i, j in problema.constraints.items()]
print(pd.DataFrame(sensibilidad))
# PUNTO C #

# Armamos la tabla de sensibilidad del problema, creando una variable que almacene una lista
# Esta lista posee un diccionario, donde mediante un ciclo for se calcularán los precio sombra y holguras
# Los precios sombras se agregan con el atributo .pi y las holguras con .slack
