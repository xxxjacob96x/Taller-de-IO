from pulp import*
import matplotlib.pyplot as plt
import numpy as np


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
problema += x1 == 2 

#resolvemos el problema con la herramienta solver 

problema.solve()

#imprimimos los resultados 
print("Estado: ", LpStatus[problema.status])
print("Valor Optimo de Z: ", problema.objective.value())
print("Valores óptimos de x1, x2:")
for variable in problema.variables():
    print(f"{variable.name}:{variable.value()}")

# Generar valores de x1 para graficar las restricciones
x1_values = np.linspace(2, 12, 400)
x2_values_1 = (96 - 12*x1_values) / 8
x2_values_2 = (72 - 6*x1_values) / 12

# Graficar las restricciones y la región factible
plt.plot(x1_values, x2_values_1, label='12*x1 + 8*x2 <= 96', color='blue')
plt.plot(x1_values, x2_values_2, label='6*x1 + 12*x2 <= 72', color='green')
plt.fill_between(x1_values, np.minimum(x2_values_1, x2_values_2), where=(x1_values >= 2), color='gray', alpha=0.5)

# Agregar la restricción x1 >= 2 como una línea vertical
plt.axvline(x=2, color='red', linestyle='--', label='x1 >= 2')

# Agregar la restricción x1 = 2 como una línea vertical
plt.axvline(x=2, color='black', linestyle=':', label='x1 = 2')

# Marcar el punto (2, 5)
plt.scatter([2], [5], color='red', label='x1=2, x2=5')

# Configurar el gráfico
plt.xlabel('x1 (Mesas)')
plt.ylabel('x2 (Sillas)')
plt.title('Región Factible del Problema de Optimización')
plt.legend()
plt.grid(True)
plt.xlim(0, 15)
plt.ylim(0, 10)

# Agregar anotaciones
plt.annotate('Región Factible', xy=(4, 3), xytext=(5, 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, horizontalalignment='left')

# Mostrar el gráfico
plt.show()
