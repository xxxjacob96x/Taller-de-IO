from pulp import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definir el problema de optimización
problema = LpProblem("Maximizar_Utilidad", LpMaximize)

# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat='Integer') #Jeans 
x2 = LpVariable("x2", lowBound=0, cat='Integer') #Franelas 

# Definir la función objetivo

problema += 400*x1 + 200*x2 , 'Z'

#Respondiendo la letra B

while True:
    try:
        
        while True:
            limite1 = int(input("Ingrese la disponibilidad nueva de Cortadores: "))

            if limite1 >= 10 and limite1 <= 20:
                break
            else:
                print("Ingrese un valor dentro del rango solicitado")

        while True:
            limite2 = int(input("Ingrese la disponibilidad nueva de Maquinas de Coser: "))

            if limite2 >= 7 and limite2 <= 18:
                break
            else:
                print("Ingrese un valor dentro del rango solicitado")

        while True:
            limite3 = int(input("Ingrese la disponibilidad nueva de Empacadores: "))

            if limite3 >= 5 and limite3 <= 16:
                break
            else:
                print("Ingrese un valor dentro del rango solicitado")
    except ValueError:
        print("Ingrese una número Valido")
        continue
    break

#cambio de restricciones en el vector de disponibilidad 

problema += 4*x1 + 2*x2  <= limite1, "Cortadores"
problema +=   x1 + 2*x2  <= limite2, "Maquinas_de_Coser" 
problema += x1 + x2 <= limite3, "Empacadores"



problema.solve()

# Imprimir el resultado
print("Estado:", LpStatus[problema.status])
print("Valor óptimo de Z:", problema.objective.value())
print("Valores óptimos de x1, x2")
for var in problema.variables():
    print(f"{var.name}: {var.value()}")

sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack} for i, j in problema.constraints.items()]

print(pd.DataFrame(sensibilidad))

# Generar valores de x1 para graficar las restricciones
x1_values = np.arange(0,15, 0.5) 
#la primera posiscion de donde empieza, de donde termina,
# 400 el numero de datos np.linspace, genera el incremento del 
#inicio al final 
x2_values_1 = (limite1 - 4*x1_values) / 2
x2_values_2 = (limite2 - x1_values) /2
x2_values_3 = (limite3 - x1_values) 


# Graficar las restricciones y la región factible
plt.plot(x1_values, x2_values_1, label='4*x1 + 2*x2 <=', color='blue')
plt.plot(x1_values, x2_values_2, label='x1 + 2*x2 <= ', color='green')
plt.plot(x1_values, x2_values_3, label='x1 + x2 <= ', color='green')

plt.fill_between(x1_values,np.minimum.reduce([x2_values_1, x2_values_2,x2_values_3]) , color='gray', alpha=0.5) #relleno entre 
#se hace el cambio por el where 
"""# np.minimun.redus, sabemos que np son son vectores, 
entonces, con los valores de prueba que se pusieron en las 
restricciones, se va a verificar entre los distintos 
vectores cuales son los minimos, esto quiere decir, 
que cumpla la restriccion menor igual"""

# Agregar la restricción x1 >= 2 como una línea vertical

# Configurar el gráfico
plt.xlabel('x1 (Jeans)')
plt.ylabel('x2 (Franela )')
plt.title('Región Factible del Problema de Optimización')
plt.legend()
#plt.grid(True)
plt.xlim(0, 15)
plt.ylim(0, 10)

# Agregar anotaciones
"""plt.annotate('Región Factible', xy=(4, 3), xytext=(5, 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, horizontalalignment='left')"""

# Mostrar el gráfico
plt.show()
