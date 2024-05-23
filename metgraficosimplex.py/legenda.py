import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 7, 10, 12]
y2 = [8, 12, 6, 9, 11]


plt.plot(x, y1, label='Serie 1(Rrestriccion 1)')
plt.plot(x, y2, label='Serie 2(Restriccion 2)')

plt.legend(loc='upper right', fontsize='medium', title='Grafico de restricciones')
#loc= ubicasion, frontsize= tamaño, title= titulo (todo eso es en relacion a la etiqueta)

#plt.legend()  # Esto muestra la leyenda basada en las etiquetas asignadas
plt.show()

"""
En el contexto de un gráfico con matplotlib, una "legenda" se refiere a una descripción o etiqueta que se muestra junto al gráfico para explicar el significado de las diferentes series de datos o elementos representados en el gráfico. La leyenda es útil cuando hay múltiples líneas, puntos, barras u otros elementos en el gráfico y se desea proporcionar una guía visual para entender qué representa cada elemento.

Para agregar una leyenda a un gráfico en matplotlib, puedes seguir estos pasos:

Asigna etiquetas a tus datos: Cuando grafiques tus datos usando matplotlib, asegúrate de asignar etiquetas a cada serie de datos utilizando el parámetro label en las funciones de trazado, como plot, scatter, bar, etc.
"""

"""
Mostrar la leyenda: Después de asignar las etiquetas, usa plt.legend() 
para mostrar la leyenda en el gráfico. matplotlib automáticamente asociará 
las etiquetas asignadas a las series de datos con las entradas de la leyenda.

La función plt.legend() toma varios argumentos opcionales para personalizar 
la apariencia de la leyenda, como la posición (loc), la orientación, el tamaño
 de fuente, el color de fondo, etc. Por ejemplo:


En el contexto de un gráfico con matplotlib, una "legenda" se refiere 
a una descripción o etiqueta que se muestra junto al gráfico para explicar 
el significado de las diferentes series de datos o elementos representados en 
el gráfico. La leyenda es útil cuando hay múltiples líneas, puntos, barras u otros
 elementos en el gráfico y se desea proporcionar una guía visual para entender qué
 representa cada elemento.

Para agregar una leyenda a un gráfico en matplotlib, puedes seguir estos pasos:

Asigna etiquetas a tus datos: Cuando grafiques tus datos usando matplotlib, 
asegúrate de asignar etiquetas a cada serie de datos utilizando el parámetro 
label en las funciones de trazado, como plot, scatter, bar, etc.

Por ejemplo:

python
Copiar código
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 15, 7, 10, 12]
y2 = [8, 12, 6, 9, 11]

plt.plot(x, y1, label='Serie 1')
plt.plot(x, y2, label='Serie 2')

plt.legend()  # Esto muestra la leyenda basada en las etiquetas asignadas
plt.show()
Mostrar la leyenda: Después de asignar las etiquetas, usa plt.legend() para mostrar la leyenda en el gráfico. matplotlib automáticamente asociará las etiquetas asignadas a las series de datos con las entradas de la leyenda.

La función plt.legend() toma varios argumentos opcionales para personalizar la apariencia de la leyenda, como la posición (loc), la orientación, el tamaño de fuente, el color de fondo, etc. Por ejemplo:

python
Copiar código
plt.legend(loc='upper right', fontsize='medium', title='Leyenda')
Esto ubicaría la leyenda en la esquina superior derecha del gráfico, 
con un tamaño de fuente mediano y un título "Leyenda". Puedes ajustar estos 
parámetros según tus necesidades.

"""