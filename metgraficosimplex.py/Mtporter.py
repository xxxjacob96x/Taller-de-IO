from pulp import *

# Definir los datos del problema
ofertas = {'A': 20, 'B': 30, 'C': 25}
demandas = {'1': 15, '2': 25, '3': 10, '4': 25}
costos = {
    ('A', '1'): 8, ('A', '2'): 6, ('A', '3'): 10, ('A', '4'): 9,
    ('B', '1'): 9, ('B', '2'): 12, ('B', '3'): 13, ('B', '4'): 7,
    ('C', '1'): 14, ('C', '2'): 9, ('C', '3'): 16, ('C', '4'): 5,
}

# Crear el problema de transporte
problema = LpProblem("Problema_de_Transporte", LpMinimize)

# Crear las variables de decisión
variable = LpVariable.dicts("Transporte", (ofertas, demandas), 0, None, cat= 'LpInteger')

# Función objetivo
problema += lpSum([costos[i, j] * variable[i][j] for i in ofertas for j in demandas])

# Restricciones de oferta
for i in ofertas:
    problema += lpSum([variable[i][j] for j in demandas]) == ofertas[i]

# Restricciones de demanda
for j in demandas:
    problema += lpSum([variable[i][j] for i in ofertas]) == demandas[j]

# Resolver el problema
problema.solve()

# Imprimir la solución
for var_prob in problema.variables():
    if var_prob.varValue > 0:
        print(f"{var_prob.name} = {var_prob.varValue}")

print(f"Costo total de transporte = {value(problema.objective)}")
