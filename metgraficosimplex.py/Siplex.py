import numpy as np
#este se encarga de imprimir el grafico 
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[1,3],[1,2],[0.5,1]])
b = np.array([42,40,15])

#Esto son los limites de la no negatividad # none es un indicador que no tienen limites dentro de la tupla
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(0, 60, 1000) #genra una lista con todo los valores para x
plt.plot(x1, (42 - x1)/3, label='x1 + 3x2 <= 42')
plt.plot(x1, (40 - x1)/2, label='x1 + 2x2 <= 40')
plt.plot(x1, (15 - 0.5*x1)/1, label='0.5x1 + x2 <= 15')

plt.fill_between(x1, 0, (42 - x1)/3, where=((42 - x1)/3 >= 0) & (x1 >= 0), alpha=0.1) 
plt.fill_between(x1, 0, (40 - x1)/2, where=((40 - x1)/2 >= 0) & (x1 >= 0), alpha=0.1)
plt.fill_between(x1, 0, (15 - 0.5*x1)/1, where=((15 - 0.5*x1)/1 >= 0) & (x1 >= 0), alpha=0.1)

plt.xlim(x1_bounds) # se utiliza para establecer los limites de los ejes x e y 
plt.ylim(x2_bounds)
plt.xlabel('Cant bolsos de mano')
plt.ylabel('Cant mochilas')
plt.legend()

#Encontrar el vértice óptimo
c = np.array([-22, -45])
res = linprog(c, A_ub=A, b_ub=b, bounds=(x1_bounds, x2_bounds), method='highs')


#Agregar el punto de la solución óptima al gráfico
vertice_optimo = (res.x[0], res.x[1])
plt.plot(vertice_optimo[0], vertice_optimo[1], 'ro', markersize=10)
plt.show()

print('El máximo se alcanza en x1 = ', res.x[0], 'y x2 = ',res.x[1], 'con un valor de ', -res.fun)

