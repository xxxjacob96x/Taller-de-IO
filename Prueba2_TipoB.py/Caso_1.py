"""
Es contratado por Mile-High Microbrewery como ingeniero industrial a cargo de la dirección
de operaciones y necesita saber qué cantidades de cerveza clara y oscura deben producir por 
día para maximizar sus ganancias. La producción de estas cervezas requiere tres tipos de recursos: 
cebada, capacidad de embotellado y mercado para la cerveza clara. A continuación, se presenta un 
resumen de los recursos necesarios y las restricciones de disponibilidad:

Productos
Recurso 	Cerveza clara 	Cerveza Oscura 	Disponibilidad diaria
Cebada 	0.1 Gramaos 	0.6 gramos 	 2000 gramos 
Embotellado 	1 Botella 	1 botella 	6000 Botellas 
Mercado 	1 Botella 		4000 botellas 
Hora Hombre 	1.5 horas 	2 horas 	5000 horas 

La ganancia por botella de cerveza clara es de $0.20 y por botella de cerveza oscura es de $0.50.
Además, por políticas de la empresa, se deben vender como mínimo 500 botellas de cerveza clara por día para evitar el sobre stock en los almacenes.

Se pide responder los siguientes puntos:
•	1) Formular el problema a mano. (5 pts)

•	2) Programar en Pulp lo formulado y encontrar la solución óptima. (5 pts)

•	3) Graficar el problema utilizando la librería de matplotlib y que incluya lo siguiente:
o	Que el grafico contenga la región del área factible sombreada (3 pts.)

o	Que el grafico contenga todas sus respectivas etiquetas de las rectas (labels).(1 pts.)

o	Que el grafico tenga los ejes debidamente nombrados y su título correspondiente. (2 pts.)

o	Que el grafico represente bien las escalas de las rectas a la gráfica adecuada. (2 pts)

•	4) Interpretar los resultados obtenidos en los puntos 2 y 3. (2 pts)


"""

#voy a hacer un ejercicio con metodo grafico 
from pulp import*
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #crear data frame, para crear una tabla
#se crea el problema de optimizacion
problema = LpProblem("Maximizar_ Ganancias", LpMaximize)

#definimos las variales de decision, 
x1= LpVariable("x1", lowBound=0, cat= LpContinuous) # Numero de botellas de cevada clara producidas por dia 
x2= LpVariable("x2", lowBound=0, cat= LpContinuous) # Numero de botellas de cevada Oscura producidas por dia 

#DEFINIMOS AHORA LA FUNCION OBJETIVO

problema += 0.2*x1 + 0.5*x2, "Z"

#ahora definimos las restricciones que son sujetas a:
problema += 0.1*x1 + 0.6*x2 <= 2000 , 'CEBADA'
problema +=   1*x1 +   1*x2 <= 6000 , 'EMBOTELLADO'
problema +=              x1 >= 500  , 'PRODUC_MIN_DE_CERVEZA_CLARA'
problema +=              x1 <= 4000 , 'MERCADO'

#resolvemos el problema con la herramienta solver 
problema.solve()

#imprimimos los resultados 
print("Estado: ", LpStatus[problema.status])
print("Valor Optimo de Z: ", problema.objective.value())
print("Valores óptimos de x1, x2:")
for variable in problema.variables():
    print(f"{variable.name}:{variable.value()}")


# === Graficar la región factible ===
# Generar valores de x1 para graficar las restricciones
x1_values = np.arange(500,100000, 100) 
#Variables del eje y 
x2_values_1 = (2000 - 0.1*x1_values) /0.6
x2_values_2 = (6000 - 1*x1_values) / 1


# Graficar las restricciones y la región factible
plt.plot(x1_values, x2_values_1, label='0.1*x1 + 0.6*x2 <= 2000', color='blue')
plt.plot(x1_values, x2_values_2, label='  1*x1 +   1*x2 <= 6000', color='green')


#plt.fill_between(x1_values,np.minimum.reduce([x2_values_1, x2_values_2] ) , color='gray', alpha=0.5) #relleno
plt.fill_between(x1_values,np.minimum.reduce([x2_values_1, x2_values_2] ) , color='gray', alpha=0.5) #relleno

#se hace el cambio por el where 

# Agregar la restricción x1 >= 2 como una línea vertical
plt.axvline(x=500, color='red', linestyle='--', label='x1 >= 500')
plt.axvline(x=4000, color='black', linestyle='--', label='x1 <= 4000')


# Configurar el gráfico
plt.xlabel('x1 (Botellas de cevada clara producidas por dia)')
plt.ylabel('x2 (Botellas de cevada oscura producidas por dia)')
plt.title('Región Factible maximizacion de Utilidad')
plt.legend()
plt.grid(True)
plt.xlim(0, 12000)
plt.ylim(0, 10000)


# Agregar anotaciones
plt.annotate('Región Factible', xy=(2000, 2000), xytext=(4500, 3500),
        arrowprops=dict(facecolor='black', arrowstyle='->'),
        fontsize=10, horizontalalignment='left')


# Mostrar el gráfico
plt.show()

"""LA SOLUCIÓN ÓPTIMA OBTENIDA REFLEJA QUE LA CANTIDAD DE BOTELLAS DE CEVADA CLARA Y OSCURAS PRODUCIDAS POR DÍA SON X1 = 3200 Y X2 = 28000 PARA
LLEGAR A UN ÓPTIMO DE $2040 PARA Z, ADEMÁS SEGÚN EL GRÁFICO, LA REGIÓN ENCERRADA ENTRE LOS LÍMITES X = 400 Y X = 4000 INDICA UN ÁREA DE OPCIONES
FÁCTIBLES QUE PODRÍA TOMAR X1 Y X2 PARA DAR SOLUCIÓN AL PROBLEMA GENERAL."""