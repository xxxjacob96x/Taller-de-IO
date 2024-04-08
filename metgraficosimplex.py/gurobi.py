import gurobipy as gp
from gurobipy import GRB

# Crear un nuevo modelo
model = gp.Model()

# Crear las variables de decisión
x = model.addVar(vtype=GRB.CONTINUOUS, name="x")
y = model.addVar(vtype=GRB.CONTINUOUS, name="y")

# Establecer la función objetivo
model.setObjective(4 * x + 3 * y, GRB.MAXIMIZE)

# Agregar las restricciones
model.addConstr(2 * x + y <= 10, "constr1")
model.addConstr(x + 2 * y <= 8, "constr2")

# Resolver el modelo
model.optimize()

# Mostrar los resultados
if model.status == GRB.OPTIMAL:
    print(f'Valor óptimo de x: {x.x}')
    print(f'Valor óptimo de y: {y.x}')
    print(f'Valor óptimo de la función objetivo: {model.objVal}')
else:
    print('El modelo no tiene solución óptima.')
