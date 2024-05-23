from pulp import *
import pandas as pd #crear data frame, para crear una tabla

# Creamos el modelo principal, indicando el sentido de la función objetivo
Problema = LpProblem("Problema de la granja", LpMinimize)

# Definimos las variables decisión y su conjunto (Ej:Continuos, Integer)
x1 = LpVariable("x1", lowBound=0, cat='Continuos')
x2 = LpVariable("x2", lowBound=0, cat='Continuos')
x3 = LpVariable("x3", lowBound=0, cat='Continuos')

# Definimos la función objetivo
Problema += 41*x1 + 36*x2 + 96*x3

#punto E
while True:
    limite1 = int(input("Ingrese la disponibilidad nueva de A: "))

    if limite1 >= 110 and limite1 <= 220:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

while True:
    limite2 = int(input("Ingrese la disponibilidad nueva de B: "))

    if limite2 >= 18 and limite2 <= 25:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

while True:
    limite3 = int(input("Ingrese la disponibilidad nueva de C: "))

    if limite3 >= 90 and limite3 <= 120:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

while True:
    limite4 = int(input("Ingrese la disponibilidad nueva de D: "))

    if limite4 >= 14 and limite4 <= 80:
        break
    else:
        print("Ingrese un valor dentro del rango solicitado")

# Definimos las restricciones del problema asociado
Problema += 20*x1 + 30*x2 + 70*x3 >= limite1, "Nutriente A"
Problema += 10*x1 + 10*x2 >= limite2, "Nutriente B"
Problema += 50*x1 + 30*x2 >= limite3, "Nutriente C"
Problema += 6*x1 + 2.5*x2 + 10*x3 >= limite4, "Nutriente D"

# Resolvemos el problema
Problema.solve()

# Imprimimos el estado final
print("Status o Estado final:", LpStatus[Problema.status])

# Imprimimos el valor de las variables
print("Valor de x1 (Cantidad de Grano #1) =", value(x1))
print("Valor de x2 (Cantidad de Grano #2) =", value(x2))
print("Valor de x3 (Cantidad de Grano #3) =", value(x3))

# Imprimimos el valor de la función objetivo
print("Valor de la función objetivo (Costo final) =", value(Problema.objective))
print()

# PUNTO C #

# Armamos la tabla de sensibilidad del problema, creando una variable que almacene una lista
# Esta lista posee un diccionario, donde mediante un ciclo for se calcularán los precio sombra y holguras
# Los precios sombras se agregan con el atributo .pi y las holguras con .slack
sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack}
               for i, j in Problema.constraints.items()]
print(pd.DataFrame(sensibilidad))


