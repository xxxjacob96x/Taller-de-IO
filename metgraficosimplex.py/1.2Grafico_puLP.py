import matplotlib.pyplot as plt
import numpy as np
from pulp import *

# Crear el problema de optimización
prob = LpProblem("Maximizar_Z", LpMaximize) #este es el modelo 

# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)

# Definir la función objetivo
prob += 3*x1 + 2*x2 + 5*x3, "Z"

# Definir las restricciones
prob += 2*x1 + x2 + x3 <= 10
prob += x1 + 2*x2 + 3*x3 <= 12

# Resolver el problema
prob.solve()

# Imprimir el resultado
print("Estado:", LpStatus[prob.status])
print("Valor óptimo de Z:", prob.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in prob.variables():
    print(f"{var.name}: {var.value()}")

# Definir las ecuaciones de las restricciones en forma de funciones
def constraint1(x):
    return (10 - 2*x)

def constraint2(x):
    return (12 - x)/2

# Crear el rango de valores para x
x_values = np.linspace(0, 10, 400)

# Calcular los valores de y para cada restricción
y_constraint1 = constraint1(x_values)
y_constraint2 = constraint2(x_values)

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Graficar las restricciones
plt.plot(x_values, y_constraint1, label='2x1 + x2 + x3 <= 10')
plt.plot(x_values, y_constraint2, label='x1 + 2x2 + 3x3 <= 12')

# Graficar la región factible (sombreada)
plt.fill_between(x_values, np.minimum(y_constraint1, y_constraint2), 0, where=(x_values>=0) & (x_values<=10), alpha=0.3, color='lightblue', label='Región Factible')


# Graficar el punto óptimo
plt.plot(value(x1), value(x2), 'ro', label='Punto óptimo')

# Etiquetas y título
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Gráfico de Restricciones y Región Factible')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
