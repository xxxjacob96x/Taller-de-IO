from pulp import *

problema = LpProblem("Maximizar_Z", LpMinimize)



# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat= "Continuous")
x2 = LpVariable("x2", lowBound=0, cat= "Continuous")
x3 = LpVariable("x3", lowBound= None,cat= "Continuous")
x4 = LpVariable("x4", lowBound= None, cat= "Continuous")

problema += x1 + x2 + x3 + x4

problema += x1 + x2 >= 6
problema += x2 + x3 -x4 <= 1
problema += 5*x1-6*x2+7*x3-8*x4 >=2

problema.solve()

print("Estado:", LpStatus[problema.status])
print("Valor óptimo de Z:", problema.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in problema.variables():
    print(f"{var.name}: {var.value()}")

