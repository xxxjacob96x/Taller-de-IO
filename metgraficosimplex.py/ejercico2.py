#voy a hacer un ejercico con metodo grafico 
from pulp import*

#se crea el problema de optimizacion
problema = LpProblem("Maximizar_Z", LpMaximize)

#definimos las variales de decision, 
x1= LpVariable("x1", lowBound=0) #MESAS
x2= LpVariable("x2", lowBound=0) #SILLAS 

#DEFINIMOS AHORA LA FUNCION OBJETIVO

problema += 5*x1 + 5*x2, "Z"

#ahora definimos las restricciones aue son Sujetas a:
problema += 12*x1 +8*x2 <= 96
problema += 6*x1 +12*x2 <= 72
problema += x1 >= 2 

#resolvemos el problema con la herramienta solver 

problema.solve()

#imprimimos los resultados 
print("Estado: ", LpStatus[problema.status])
print("Valor Optimo de Z: ", problema.objective.value())
print("Valores óptimos de x1, x2:")
for variable in problema.variables():
    print(f"{variable.name}:{variable.value()}")

"""
ahora para poder imprimir el resultado, utilizamos los comandos 
LpStatus que traduce el código de estado numérico del problema 
el comando que hace el llamado es .status 
para hallar el valor optimo del problema osea Z utilizamos 
objetive.value que te da el valor de la función objetivo 
en el punto óptimo encontrado por el solver.
tambien nosotros tenemos que describir los valores de 
la restriccion, o sea mostrar las variables.

luego de eso realizamos un bucle for para llamar a la varaile 
de la funcion

"""