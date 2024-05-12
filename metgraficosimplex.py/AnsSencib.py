#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''International Wool Company opera en una gran granja en donde se crian ovejas. El Administrador de la
granja ha determinado que para que sus ovejas crezcan de una forma deseada, estos necesitan como mínimo
una cantidad de nutrientes especificicas (Los nutrientes no son tóxicos para las ovejas, por lo que pueden
consumir más del minimo sin sufrir daños). El administrador considera tres diferentes tipos de granos para
alimentar a las ovejas. La tabla B-2 lista el número de unidades por cada nutriente y por cada libra de
granos. Además, se muestra el minimo de unidades requeridas para consumir de cada nutriente. y por último
se muestra el costo por libra de cada grano. El administrador cree que cada oveja debe recibir una cantidad
minima de cada nutriente para conseguir que crezcan sanas y produzcan una cantidad estándar de lana. El
Administrador quiere que cada oveja crezca al mínimo costo'''

'''EJEMPLO DE EVALUACIÓN:

PARTE #1
A) FORMULE EL PROBLEMA
B) ENCUENTRE LA SOLUCIÓN ÓPTIMA DEL PROBLEMA BASE UTILIZANDO LA LIBRERÍA DE PULP
C) CÁLCULE LA TABLA DE ANÁLISIS DE SENSIBILIDAD
D) INTERPRETE LOS RESULTADOS OBTENIDOS DEL PUNTO B Y C SEGÚN EL CONTEXTO DEL PROBLEMA, 
MEDIANTE UN PRINT 
(ESCRIBA UN COMENTARÍO EN PYTHON)

PARTE #2
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
LAS UNIDADES TOTALES REQUERIDAS POR ESTE MISMO.

'''


# PROBLEMA GENERAL
# 
# ![Ej1.png](attachment:Ej1.png)

# #PARTE 1: MODELO A OPTIMIZAR PUNTO A
# 
# ![Model1.png](attachment:Model1.png)

# In[5]:


# PUNTO B #

## Importamos pulp para armar el modelo de programación lineal
## Importamos pandas para crear un dataframe que cálcule el análisis de sensibilidad
import pulp
import pandas as pd #crear data frame, para crear una tabla

# Creamos el modelo principal, indicando el sentido de la función objetivo
model = pulp.LpProblem("Problema de la granja", pulp.LpMinimize)

# Definimos las variables decisión y su conjunto (Ej:Continuos, Integer)
x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuos')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuos')
x3 = pulp.LpVariable("x3", lowBound=0, cat='Continuos')

# Definimos la función objetivo
model += 41*x1 + 36*x2 + 96*x3

# Definimos las restricciones del problema asociado
model += 20*x1 + 30*x2 + 70*x3 >= 110, "Nutriente A"
model += 10*x1 + 10*x2 >= 18, "Nutriente B"
model += 50*x1 + 30*x2 >= 90, "Nutriente C"
model += 6*x1 + 2.5*x2 + 10*x3 >= 14, "Nutriente D"

# Resolvemos el problema
model.solve()

# Imprimimos el estado final
print("Status o Estado final:", pulp.LpStatus[model.status])

# Imprimimos el valor de las variables
print("Valor de x1 (Cantidad de Grano #1) =", pulp.value(x1))
print("Valor de x2 (Cantidad de Grano #2) =", pulp.value(x2))
print("Valor de x3 (Cantidad de Grano #3) =", pulp.value(x3))

# Imprimimos el valor de la función objetivo
print("Valor de la función objetivo (Costo final) =", pulp.value(model.objective))
print()

# PUNTO C #

# Armamos la tabla de sensibilidad del problema, creando una variable que almacene una lista
# Esta lista posee un diccionario, donde mediante un ciclo for se calcularán los precio sombra y holguras
# Los precios sombras se agregan con el atributo .pi y las holguras con .slack
sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack}
               for i, j in model.constraints.items()]
print(pd.DataFrame(sensibilidad))

# PUNTO D #

'''Los valores obtenidos indican que el óptimo que toma la función objetivo para reducir el costo total
esta dado por $148.61, en donde las cantidades de grano a consumir por oveja son:
x1 = 0.59
x2 = 2.00
x3 = 0.54

Por otro lado observamos que si aumentamos en una unidad en el lado derecho de la restricción 4 
obtendríamos una solución óptima de $148.61 + 3.61

Una de las restricciones no se está cumpliendo en la solución óptima, dado que arroja una holgura negativa.

'''


