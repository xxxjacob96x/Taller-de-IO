#voy a hacer un ejercico con metodo grafico 
from pulp import*
import numpy as np
import matplotlib.pyplot as plt

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

#======= EXPLICASION_GRAFICO ==========#
#primero: definimos el eje x
x1_values = np.arange(2,12, 0.5)

#segundo: definimos el eje y 

x2_values_1 = (96 - 12*x1_values) / 8
x2_values_2 = (72 - 6*x1_values) / 12

# Graficar las restricciones y la region factible 

plt.plot(x1_values,x2_values_1, label= '12x1+8x2<=96', color= 'blue')
plt.plot(x1_values,x2_values_2, label= '6x1+12x2<=72', color= 'green')
plt.fill_between(x1_values,np.minimum.reduce([x2_values_1,x2_values_2]), color ='gray', alpha = 0.5)

plt.axvline(x=2, color= 'red', linestyle = '--', label ='x1>=2')

# Configuracion del Grafico 
plt.xlabel('x1 (Mesas)')
plt.ylabel('x2 (Sillas)')
plt.title('Region Factible del Problema de produccion de mesas y sillas')
plt.legend()
plt.grid(True)
plt.xlim(0,15)
plt.ylim(0,10)

plt.show()