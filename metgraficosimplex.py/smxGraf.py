import numpy as np
import matplotlib.pyplot as plt

# Definir las restricciones
def constraint1(x1):
    return (10 - 2*x1)

def constraint2(x1):
    return (12 - x1)/2

# Generar puntos para graficar las restricciones
x1_values = np.linspace(0, 6, 100)
y_constraint1 = constraint1(x1_values)
y_constraint2 = constraint2(x1_values)

# Graficar las restricciones
plt.plot(x1_values, y_constraint1, label="2x1 + x2 + x3 = 10")
plt.plot(x1_values, y_constraint2, label="x1 + 2x2 + 3x3 = 12")

# Graficar la región factible
plt.fill_between(x1_values, 0, y_constraint1, where=(y_constraint1 >= 0), alpha=0.3)
plt.fill_between(x1_values, 0, y_constraint2, where=(y_constraint2 >= 0), alpha=0.3)

# Etiquetas y leyenda
plt.xlabel("x1")
plt.ylabel("x2, x3")
plt.title("Región Factible")
plt.legend()

# Mostrar el gráfico
plt.show()
