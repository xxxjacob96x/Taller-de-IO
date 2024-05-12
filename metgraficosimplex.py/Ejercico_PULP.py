from pulp import * 

#Defenimos el problema de programacion lineal 

problema = LpProblem("Problema_Optimizacio_PL", LpMaximize)
#Ingresamos las variables que entraran en el sistema, ya sea X1, X2, tec.

x1 = LpVariable("X1", lowBound=0 , cat= 'Integer')
x2 = LpVariable("X2", lowBound=0 , cat= 'Integer')

#se define la Funcion Objetivo 

problema += 2*x1-4*x2

# Restriccion S.a

problema += -x1  +  x2 <=3
problema += -x1  +2*x2 >=-3
problema += 3*x1 +  x2 == 3

#Ahora desarrollamos el solver para ejecutarlo 

problema.solve()

print("")
print("El optimo se obtiene con x1= ", x1.varValue, "y x2= ",x2.varValue, "El optimo de Z es: ",problema.objective.value() )


""" 
Se inicia definiendo el problema con LpProblem como funcion de Pulp

LpMaximize es la funcion que se utiliza en pulp
para el caso de minimizacion en el modulo de PULP es cambiar el mx por el in "LpMimize"

LpVariable es una funcion del pulp para definir una varable 

lowBound, tambien es una funcion de pulp que permite ingresar la no negatividad del problem 
(lowBound: Este parámetro define el límite inferior para las variables. En tu código, 
has establecido el límite inferior en 0 para x1 y x2, lo que significa que no pueden tomar valores negativos.)

cat, otra funcion, es un parámetro utilizado al definir variables en PuLP. 
Indica la categoría o tipo de la variable en el problema de programación lineal. 
En este caso, 'Integer' especifica que las variables x1 y x2 son variables enteras (números enteros) en lugar de variables continuas.

'Integer',significa que las variables x1 y x2 son variables enteras (números enteros). 
Otras categorías comunes incluyen 'Continuous' (variables continuas) y 'Binary' (variables binarias).

varValue: Esta es una propiedad de las variables en PuLP que te permite acceder al valor óptimo al que 
la variable se ha resuelto después de resolver el problema de programación lineal. 
Por ejemplo, x1.varValue te da el valor óptimo de x1 después de resolver el problema.

La parte problema.objective.value() devuelve el valor óptimo de la función objetivo, es decir,
el valor de la función objetivo cuando las variables toman los valores óptimos encontrados por el solver.

"""