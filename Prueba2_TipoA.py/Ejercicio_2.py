"""
CASO 2 (20 pts)
Suponga que una empresa necesita saber qué cantidades de productos diferentes A y B necesita 
producir por día para maximizar sus ganancias, en donde (para su elaboración) se necesita 4 entradas 
o inputs, siendo estas horas-hombre, material del tipo L, material del tipo M y material del tipo H. 
Para producir una unidad del producto A se requieren 4 kg del material L, 500 gr del material M, 6kg 
del material H y 8 horas de HH. Para producir una unidad del producto B se requieren 10kg del 
material L, 800 gr del material M, 8kg del material H y 12 horas de HH. La empresa gana por concepto 
de utilidad $20.000 por el producto A y $40.000 por el producto B.
Considere que en bodega solo hay 80 kg del material L, 20 kg del material M, 40 kg del material y la 
empresa cuenta con 150 horas de hh disponibles (por día) para realizar el trabajo. Además (por 
políticas de la empresa), se debe vender como mínimo 4 productos de A por día, esto debido a que se 
evita el sobre stock en los almacenes.
considere 1kg = 1000gr
Se pide:
• 1) Formular el problema a mano. (5 pts)
• 2) Programar en Pulp lo formulado y encontrar la solución óptima. (5 pts)
• 3) Graficar el problema utilizando la librería de matplotlib. (8 pts)
• 4) Interpretar los resultados obtenidos en los puntos 2 y 3. (2 pts)
Considere que la gráfica debe tener los títulos, etiquetas (labels), tamaño, colores y configuraciones 
adecuadas para su presentación.


"""

#voy a hacer un ejercico con metodo grafico 
from pulp import*
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #crear data frame, para crear una tabla
#se crea el problema de optimizacion
problema = LpProblem("Maximizar_ Ganancias", LpMaximize)

#definimos las variales de decision, 
x1= LpVariable("x1", lowBound=0, cat= LpInteger) #PRODUCTO A
x2= LpVariable("x2", lowBound=0, cat= LpInteger) #PRODUCTO B

#DEFINIMOS AHORA LA FUNCION OBJETIVO

problema += 20000*x1 + 40000*x2, "Z"

#ahora definimos las restricciones aue son Sujetas a:
problema += 4*x1 +10*x2 <= 80, 'ML'
problema += 0.5*x1 +0.8*x2 <= 20, 'MM'
problema += 6*x1 +8*x2 <= 40 , 'MH'
problema += 8*x1 +12*x2 <= 150 ,'HH'
problema += x1 >= 4 

#resolvemos el problema con la herramienta solver 

problema.solve()

#imprimimos los resultados 
print("Estado: ", LpStatus[problema.status])
print("Valor Optimo de Z: ", problema.objective.value())
print("Valores óptimos de x1, x2:")
for variable in problema.variables():
    print(f"{variable.name}:{variable.value()}")

sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack}
               for i, j in problema.constraints.items()]
print(pd.DataFrame(sensibilidad))

# === Graficar la región factible ===
# Generar valores de x1 para graficar las restricciones
x1_values = np.arange(4,40, 0.05) 
#Variables del eje y 
x2_values_1 = (80 - 4*x1_values) / 10
x2_values_2 = (20 - 0.5*x1_values) / 0.8
x2_values_3 = (40 - 6*x1_values) / 8
x2_values_4 = (150 - 8*x1_values) /12

# Graficar las restricciones y la región factible
plt.plot(x1_values, x2_values_1, label='4*x1 + 10*x2 <= 80', color='blue')
plt.plot(x1_values, x2_values_2, label='0.5*x1 + 0.8*x2 <= 20', color='green')
plt.plot(x1_values, x2_values_3, label='6*x1 + 8*x2 <= 40', color='pink')
plt.plot(x1_values, x2_values_4, label='8*x1 + 12*x2 <= 150', color='yellow')

plt.fill_between(x1_values,np.minimum.reduce([x2_values_1, x2_values_2,x2_values_3,x2_values_4] ) , color='gray', alpha=0.5) #relleno entre 
#se hace el cambio por el where 

# Agregar la restricción x1 >= 2 como una línea vertical
plt.axvline(x=4, color='red', linestyle='--', label='x1 >= 4')

# Configurar el gráfico
plt.xlabel('x1 (Producto A)')
plt.ylabel('x2 (Producto B)')
plt.title('Cantidades a producir del producto A y B')
plt.legend()
plt.grid(True)
plt.xlim(0, 40)
plt.ylim(0, 25)

# Agregar anotaciones
plt.annotate('Región Factible', xy=(4.2, 0.5), xytext=(15, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, horizontalalignment='left')

# Mostrar el gráfico
plt.show()
