from pulp import *
import pandas as pd

# Definir el problema de optimización
prob = LpProblem("Maximizar_Utilidad", LpMaximize)

# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat=LpContinuous)
x2 = LpVariable("x2", lowBound=0, cat=LpContinuous)
x3 = LpVariable("x3", lowBound=0, cat=LpContinuous)

# Definir la función objetivo
prob += 400*x1 + 200*x2 + 300*x3, 'Z'

# Definir las restricciones
prob += 4*x1 + 2*x2 + x3 <= 16, "Cortadores"
prob += x1 + 2*x2 + 2*x3 <= 41, "Maquinas_de_Coser" 
prob += x1 + x2 + x3 <= 16, "Empacadores"

# Resolver el problema
prob.solve()

# Imprimir el resultado
print("Estado:", LpStatus[prob.status])
print("Valor óptimo de Z:", prob.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in prob.variables():
    print(f"{var.name}: {var.value()}")

# Análisis de sensibilidad
sensibilidad = [{'Restriccion': i, 'Precio Sombra': j.pi, 'Holgura': j.slack} for i, j in prob.constraints.items()]
print(pd.DataFrame(sensibilidad))
