from pulp import LpMaximize, LpProblem, LpVariable

# Crear el problema de optimización
prob = LpProblem("Maximizar_Z", LpMaximize)

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
print("Estado:", LpProblem.status[prob.status])
print("Valor óptimo de Z:", prob.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in prob.variables():
    print(f"{var.name}: {var.value()}")
