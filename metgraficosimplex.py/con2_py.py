"""PARTE #2
AHORA, SUPONGA QUE EL GRANJERO DESEA CAMBIAR LAS UNIDADES TOTALES MÍNIMAS REQUERIDAS PARA
ALIMENTAR A SUS OVEJAS, POR LO QUE LE GUSTARÍA AVERIGUAR EL IMPACTO TOTAL QUE TENDRÍA SOBRE
SUS COSTOS.

E) CONSIDERANDO EL CASO ANTERIOR VUELVA A CALCULAR LA SOLUCIÓN ÓPTIMA DEL PROBLEMA CONSIDERANDO 
LA CANTIDADES TOTALES MÍNIMAS REQUERIDAS DE FORMA VARIABLE, CONSIDERANDO LOS SIGUIENTES RANGOS
PARA SU EVALUACIÓN:

    NUTRIENTE A: [110,220], SI NO FUERA DE RANGO
    NUTRIENTE B: [18,25], SI NO FUERA DE RANGO
    NUTRIENTE C: [90,120], SI NO FUERA DE RANGO
    NUTRIENTE D: [14, 80], SI NO FUERA DE RANGO
    
F) ENTREGUE LA TABLA DE ANÁLISIS DE SENSIBILIDAD PARA CADA CAMBIO

NOTA: PARA EL PUNTO E SE DEBE SOLICITAR AL USUARIO (MEDIANTE UN INPUT) LOS DATOS QUE REPRESENTARÍAN
LAS UNIDADES TOTALES REQUERIDAS POR ESTE MISMO."""

# In[3]:

import pulp
import pandas as pd

# Creamos el modelo principal, indicando el sentido de la función objetivo
model = pulp.LpProblem("Problema de optimización", pulp.LpMinimize)

# Definimos las variables decisión y su conjunto (Ej:Continuos, Integer)
x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuos')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuos')
x3 = pulp.LpVariable("x3", lowBound=0, cat='Continuos')

# Definimos la función objetivo
model += 41*x1 + 36*x2 + 96*x3

# PUNTO E #

# Definimos los recursos disponibles
while True:
    Limite1 = int(input("Ingrese la cantidad limitante de la restricción 1: "))
    
    if Limite1 >= 110 and Limite1 <= 220:
        break
    else:
        print("Fuera de rango, ingrese otro valor: ")

while True:
    Limite2 = int(input("Ingrese la cantidad limitante de la restricción 2: "))
    
    if Limite2 >= 18 and Limite2 <= 25:
        break
    else:
        print("Fuera de rango, ingrese otro valor: ")
        
while True:
    Limite3 = int(input("Ingrese la cantidad limitante de la restricción 3: "))
    
    if Limite3 >= 90 and Limite3 <= 120:
        break
    else:
        print("Fuera de rango, ingrese otro valor: ")
    
while True:
    Limite4 = int(input("Ingrese la cantidad limitante de la restricción 4: "))
    
    if Limite4 >= 14 and Limite4 <= 80:
        break
    else:
        print("Fuera de rango, ingrese otro valor: ")


# Definimos las restricciones del problema asociado
model += 20*x1 + 30*x2 + 70*x3 >= Limite1, "Restricción 1"
model += 10*x1 + 10*x2 >= Limite2, "Restricción 2"
model += 50*x1 + 30*x2 >= Limite3, "Restricción 3"
model += 6*x1 + 2.5*x2 + 10*x3 >= Limite4, "Restricción 4"

# Resolvemos el problema
model.solve()

# Imprimimos el estado final
print()
print("Status o Estado final:", pulp.LpStatus[model.status])

# Imprimimos el valor de las variables
print("Valor de x1 (Cantidad de Grano #1) =", pulp.value(x1))
print("Valor de x2 (Cantidad de Grano #2) =", pulp.value(x2))
print("Valor de x3 (Cantidad de Grano #3) =", pulp.value(x3))

# Imprimimos el valor de la función objetivo
print("Valor de la función objetivo (Costo final) =", pulp.value(model.objective))
print()

# PUNTO F #

# Armamos la tabla de sensibilidad del problema, creando una variable que almacene una lista
# Esta lista posee un diccionario, donde mediante un ciclo for se calcularán los precio sombra y holguras
# Los precios sombras se agregan con el atributo .pi(Precio sombra o shadow price) y las holguras con .slack(holgura)
sensibilidad = [{'Restricción':i,'Precio Sombra': j.pi, 'Holgura': j.slack}
               for i, j in model.constraints.items()]
print(pd.DataFrame(sensibilidad))


# In[ ]:
