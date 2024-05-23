import networkx as nx
import matplotlib.pyplot as plt
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

# Crear un gráfico de red
G = nx.DiGraph()

# Añadir nodos para ofertas y demandas
for oferta in ofertas:
    G.add_node(oferta, pos=(0, list(ofertas.keys()).index(oferta)))
    
for demanda in demandas:
    G.add_node(demanda, pos=(1, list(demandas.keys()).index(demanda)))

# Añadir aristas para las rutas con cantidades y costos
for (i, j), costo in costos.items():
    if f"Transporte_{i}_{j}" in solucion:
        G.add_edge(i, j, weight=costo, label=f"{solucion[f'Transporte_{i}_{j}']} ({costo})")

# Posiciones de los nodos
pos = nx.get_node_attributes(G, 'pos')

# Dibujar el gráfico
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title('Gráfico de Red del Problema de Transporte')
plt.show()
