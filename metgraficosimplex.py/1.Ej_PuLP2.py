from pulp import * 
"""LpMaximize, LpProblem, LpVariable, LpStatus"""

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
"""print("Estado:", LpProblem.status[prob.status])"""
print("Estado:", LpStatus[prob.status])
print("Valor óptimo de Z:", prob.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in prob.variables():
    print(f"{var.name}: {var.value()}")



"""
La función LpStatus[prob.status] traduce el código de estado numérico del problema (prob.status) 
en una representación más legible. Por ejemplo, si el estado es 1, que significa "Óptimo", 
esta línea imprimirá "Estado: Optimal".


El método prob.objective.value() te da el valor de la función objetivo 
en el punto óptimo encontrado por el solver.

print(f"{var.name}: {var.value()}"): Dentro del bucle, esta línea imprime el nombre y
el valor óptimo de cada variable. 
Por ejemplo, si x1 tiene un valor óptimo de 2, x2 tiene un valor óptimo de 3 y x3 tiene un 
valor óptimo de 4, esta línea imprimirá algo como "x1: 2", "x2: 3", "x3: 4".


La f que aparece antes de las comillas dobles en la línea print(f"{var.name}: {var.value()}") 
indica una cadena de formato f. Esto es parte de las f-strings, una característica introducida 
en Python 3.6 que permite formatear cadenas de manera más conveniente y legible.

En una f-string, puedes incluir expresiones dentro de llaves {} directamente dentro de la cadena, 
y Python evaluará esas expresiones y las sustituirá por sus valores al imprimir la cadena. 
Por ejemplo:

{var.name}: Aquí, var.name es una expresión que se evalúa para obtener el nombre de la variable var.

{var.value()}: Esta es otra expresión que se evalúa para obtener el valor de la variable var.

Entonces, en el contexto de la línea print(f"{var.name}: {var.value()}"), la f-string está 
formateando la cadena de tal manera que se imprime el nombre de la variable (var.name) 
seguido por : y luego el valor de la variable (var.value()). 
Esto hace que la salida sea más clara y fácil de entender al mostrar el nombre y el valor de 
cada variable de decisión en el problema de optimización.

"""