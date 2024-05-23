from pulp import *
import matplotlib.pyplot as plt

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
variable = LpVariable.dicts("Transporte", (ofertas, demandas), 0, None, cat='LpInteger')

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
solucion = {}
for var_prob in problema.variables():
    if var_prob.varValue > 0:
        solucion[var_prob.name] = var_prob.varValue
        print(f"{var_prob.name} = {var_prob.varValue}")

print(f"Costo total de transporte = {value(problema.objective)}")

# Crear una gráfica
plt.figure(figsize=(10, 7))

# Posiciones de las ofertas y demandas para el gráfico
pos_ofertas = {'A': (0, 2), 'B': (0, 1), 'C': (0, 0)}
pos_demandas = {'1': (3, 3), '2': (3, 2), '3': (3, 1), '4': (3, 0)}

# Dibujar las ofertas y demandas en el gráfico
for oferta, (x, y) in pos_ofertas.items():
    plt.scatter(x, y, color='blue', s=500)
    plt.text(x - 0.2, y, oferta, fontsize=12, ha='center', va='center', color='white')
    
for demanda, (x, y) in pos_demandas.items():
    plt.scatter(x, y, color='green', s=500)
    plt.text(x + 0.2, y, demanda, fontsize=12, ha='center', va='center', color='white')

# Dibujar las rutas y los costos
for (i, j), costo in costos.items():
    x_oferta, y_oferta = pos_ofertas[i]
    x_demanda, y_demanda = pos_demandas[j]
    plt.plot([x_oferta, x_demanda], [y_oferta, y_demanda], 'k--', alpha=0.5)
    
    transporte_var = f"Transporte_{i}_{j}"
    if transporte_var in solucion:
        plt.text((x_oferta + x_demanda) / 2, (y_oferta + y_demanda) / 2, f"{solucion[transporte_var]} ({costo})",
                 fontsize=10, color='red', ha='center', va='center')

plt.xlabel('Ubicación')
plt.ylabel('Nivel')
plt.title('Solución del Problema de Transporte')
plt.grid(True)
plt.show()
