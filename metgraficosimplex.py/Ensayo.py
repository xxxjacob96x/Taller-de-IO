import pulp
import matplotlib.pyplot as plt
import numpy as np

# Crear el problema de maximización
model = pulp.LpProblem("Maximizar_Ganancias", pulp.LpMaximize)

# Definir las variables de decisión
x = pulp.LpVariable('x', lowBound=500, cat='Continuous')  # Cerveza clara
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')    # Cerveza oscura

# Definir la función objetivo
model += 0.20 * x + 0.50 * y, "Ganancia_Total"

# Definir las restricciones
model += 0.1 * x + 0.6 * y <= 2000, "Restriccion_Cebada"
model += x + y <= 6000, "Restriccion_Embotellado"
model += x <= 4000, "Restriccion_Mercado_Cerveza_Clara"

# Resolver el problema
model.solve()

# Imprimir los resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Botellas de Cerveza Clara: {x.varValue}")
print(f"Botellas de Cerveza Oscura: {y.varValue}")
print(f"Ganancia Total: ${pulp.value(model.objective)}")

# Graficar las restricciones y la región factible
x_vals = np.linspace(500, 6000, 400)

# Restricciones
y1 = (2000 - 0.1 * x_vals) / 0.6
y2 = 6000 - x_vals
y3 = np.full_like(x_vals, 4000)

plt.figure(figsize=(10, 8))
plt.plot(x_vals, y1, label=r'$0.1x + 0.6y \leq 2000$')
plt.plot(x_vals, y2, label=r'$x + y \leq 6000$')
plt.axvline(4000, color='red', linestyle='--', label=r'$x \leq 4000$')
plt.axvline(500, color='green', linestyle='--', label=r'$x \geq 500$')

# Rellenar la región factible
plt.fill_between(x_vals, 0, np.minimum(y1, y2), where=(x_vals >= 500) & (x_vals <= 4000), color='gray', alpha=0.3)

# Límites de la gráfica
plt.xlim(0, 6500)
plt.ylim(0, 3500)

# Solución óptima
plt.plot(x.varValue, y.varValue, 'ro', markersize=10)
plt.text(x.varValue, y.varValue, f'({x.varValue}, {y.varValue})', fontsize=12, verticalalignment='bottom')

# Etiquetas y leyenda
plt.xlabel('Botellas de Cerveza Clara')
plt.ylabel('Botellas de Cerveza Oscura')
plt.title('Optimización de Producción de Cerveza en Mile-High Microbrewery')
plt.legend()
plt.grid(True)
plt.show()
