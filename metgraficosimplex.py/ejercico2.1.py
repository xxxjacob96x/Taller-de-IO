#voy a hacer un ejercico con metodo grafico 
from pulp import*
import numpy as np
import matplotlib.pyplot as plt

#se crea el problema de optimizacion
problema = LpProblem("Maximizar_Z", LpMaximize)

#definimos las variales de decision, 
x1= LpVariable("x1", lowBound=0) #MESAS
x2= LpVariable("x2", lowBound=0) #SILLAS 

#DEFINIMOS AHORA LA FUNCION OBJETIVO

problema += 5*x1 + 5*x2, "Z"

#ahora definimos las restricciones aue son Sujetas a:
problema += 12*x1 +8*x2 <= 96
problema += 6*x1 +12*x2 <= 72
problema += x1 >= 2 

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
x1_values = np.arange(2,12, 0.05) 
#la primera posiscion de donde empieza, de donde termina,
# 400 el numero de datos np.linspace, genera el incremento del 
#inicio al final 
x2_values_1 = (96 - 12*x1_values) / 8
x2_values_2 = (72 - 6*x1_values) / 12

# Graficar las restricciones y la región factible
plt.plot(x1_values, x2_values_1, label='12*x1 + 8*x2 <= 96', color='blue')
plt.plot(x1_values, x2_values_2, label='6*x1 + 12*x2 <= 72', color='green')
plt.fill_between(x1_values,np.minimum.reduce([x2_values_1, x2_values_2]) , color='gray', alpha=0.5) #relleno entre 
#se hace el cambio por el where 
"""# np.minimun.redus, sabemos que np son son vectores, 
entonces, con los valores de prueba que se pusieron en las 
restricciones, se va a verificar entre los distintos 
vectores cuales son los minimos, esto quiere decir, 
que cumpla la restriccion menor igual"""

# Agregar la restricción x1 >= 2 como una línea vertical
plt.axvline(x=2, color='red', linestyle='--', label='x1 >= 2')

# Configurar el gráfico
plt.xlabel('x1 (Mesas)')
plt.ylabel('x2 (Sillas)')
plt.title('Región Factible del Problema de Optimización')
plt.legend()
#plt.grid(True)
plt.xlim(0, 15)
plt.ylim(0, 10)

# Agregar anotaciones
plt.annotate('Región Factible', xy=(4, 3), xytext=(5, 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, horizontalalignment='left')

# Mostrar el gráfico
plt.show()


"""
=== plt.grid(True): Esta línea activa la visualización 
de una cuadrícula en el gráfico. La cuadrícula puede ayudar a los usuarios 
a leer y entender mejor los valores en el gráfico al proporcionar líneas de 
referencia horizontales y verticales.

=== plt.xlim(0, 15): Esta línea establece los límites del eje x del gráfico, 
especificando que el eje x debe ir desde 0 hasta 15. Esto significa que el
gráfico solo mostrará valores de x en este rango.

=== plt.ylim(0, 10): Similarmente, esta línea establece los límites del 
eje y del gráfico, especificando que el eje y debe ir desde 0 hasta 10. 
Esto significa que el gráfico solo mostrará valores de y en este rango.

========== ANOTACION DE LA LINEA NEGRA PARA MAYOR PROFECIONALIDAD =========

La función annotate de la biblioteca matplotlib.pyplot para añadir una anotación en un gráfico.
 Vamos a desglosar cada uno de sus componentes:

=== plt.annotate('Región Factible', ...): Esta función añade una anotación con 
el texto "Región Factible" en el gráfico.

=== xy=(4, 3): Define la posición (x, y) en el gráfico donde se coloca la anotación. 
En este caso, la anotación se coloca en la coordenada (4, 3).

=== xytext=(5, 4): Define la posición (x, y) donde se colocará el texto de la anotación. 
En este caso, el texto se coloca en la coordenada (5, 4), ligeramente desplazado 
de la posición de la anotación.

=== arrowprops=dict(facecolor='black', arrowstyle='->'): Este diccionario especifica 
las propiedades de la flecha que conecta el texto de la anotación con la posición anotada. 
Aquí, facecolor='black' define el color de la flecha como negro, y arrowstyle='->' define 
el estilo de la flecha como una simple flecha que apunta.

==== fontsize=10: Define el tamaño de la fuente del texto de la anotación. 
En este caso, el tamaño de la fuente es 10.

=== horizontalalignment='left': Define la alineación horizontal del texto. 
Aquí, el texto está alineado a la izquierda de la posición xytext.

"""