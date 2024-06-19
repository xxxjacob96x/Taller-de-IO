"""
Una fábrica de ropa produce 3 líneas de traje: jeans, franela y amasado. 
La ropa es vendida en lotes de 100 trajes. Cada lote pasa a través de 3 procesos: corte, cocido y empaque. 
La planta dispone de 16 cortadores 41 máquinas de coser y 20 hola empacadores. 
Los requerimientos para producir un lote de 100 trajes de cada línea y las utilidades asociadas se presentan a continuación:

Requerimientos de produccion             | jeans    | Franelas  | Amasados 
Cortadores [personas/ lote]              |  4       |   2       |   1
Hola máquinas de coser [máquinas/ lote]  |  1       |   2       |   2
Empacadores [personas/ lote]             |  1       |   1       |   1
Utilidad [USD /lote]                     |  400     | 200       |   300

a. Formule para hallar el máximo beneficio de este problema.
b. Realice una condición con el fin de mover los vectores de disponibilidad.
c. ¿Es posible despedir cortadores o empaquetadores manteniendo el nivel de producción?¿Cuántos?
d. La empresa puede contratar cortadores adicionales a un precio de US$280 cada uno. 
¿Cuánta mano de obra a este precio estaría dispuesto a contratar la empresa? ¿Cómo cambia la solución óptima?
e. Suponga que un cambio en la tecnología de fabricación requiere agregar un proceso de lavado. Los requerimientos de lavado para producir lotes de 100 Unidades. De cada tipo de traje y la disponibilidad máxima de lavado de detallan a continuación.

Requerimientos de produccion             | jeans    | Franelas  | Amasados | Disp. Max
Lavadores [personas/ lote]               |  3       |   3       |   2      | 40 personas
"""
# desarrollo del problema en general 
from pulp import *
import pandas as pd

# Definir el problema de optimización
prob = LpProblem("Maximizar_Utilidad", LpMaximize)

# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat='Continuous')
x2 = LpVariable("x2", lowBound=0, cat='Continuous')
x3 = LpVariable("x3", lowBound=0, cat='Continuous')

# Definir la función objetivo
prob += 400*x1 + 200*x2 + 300*x3, 'Z'

# Definir las restricciones
prob += 4*x1 + 2*x2 + x3 <= 16, "Cortadores"
prob += x1 + 2*x2 + 2*x3 <= 41, "Maquinas_de_Coser" 
prob += x1 + x2 + x3 <= 20, "Empacadores"

# Resolver el problema
prob.solve()

# Imprimir el resultado
print("Estado:", LpStatus[prob.status])
print("Valor óptimo de Z:", prob.objective.value())
print("Valores óptimos de x1, x2, x3:")
for var in prob.variables():
    print(f"{var.name}: {var.value()}")

sensibilidad = [{'Restriccion':i, 'precio Sombra': j.pi, 'Holgura': j.slack } for i, j in prob.constraints.items()]
print(pd.DataFrame(sensibilidad))