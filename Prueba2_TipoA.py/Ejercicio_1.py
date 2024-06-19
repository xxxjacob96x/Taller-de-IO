"""
Suponga que usted trabaja en una empresa que elabora todo tipo de jugos que son distribuidos por 
empresas externas hacia supermercados, almacenes y empresas. En la actualidad, la gerencia de la 
empresa se encuentra realizando el diseño de un nuevo tipo de jugo bisabor (Naranja – Plátano) en 
donde su principal objetivo es conseguir que su contenido tenga una mezcla equilibrada de ciertos 
componentes que logren elaborar este jugo con la máxima calidad posible realizándolo al menor 
precio, es por esto que se le ha encargado al Ing. Industrial del departamento de operaciones y 
calidad (usted) que determiné la mejor composición química del jugo considerando que en un inicio 
se buscaba que tuviera una composición de 10 - 12 - 8 - 4 (El jugo contiene una composición de a% 
- b% - c% y d%, donde a% es el porcentaje de naranja, b% el porcentaje de plátano, c% el 
porcentaje de leche y d% el porcentaje de aditivos, considere el resto de los porcentajes del jugo no 
influyente en el sabor del jugo).

Para realizar este trabajo, el Ing. Industrial ha recopilado (gracias al químico de la empresa) cierta 
información de los contenidos porcentuales del mismo jugo bisabor (Naranja – Plátano) de cuatro 
empresas distintas, esto con la finalidad de determinar que la composición final del producto será un 
mix de los 4 productos distintos. El químico exige que la composición porcentual de cada elemento 
del jugo varie como máximo en un 10% desde la composición planteada en un inicio, esto significa 
que el porcentaje del jugo de naranja no puede superar (límite superior) el 11% del contenido ni ser 
menor al 10% (límite inferior).

Los objetivos del ingeniero industrial es determinar la mejor composición química del mix para 
conseguir un kilogramo de la mezcla del producto final para que pueda ser evaluado por el químico 
de la empresa.

Considere para la programación:

Restricción X < = Límite Inferior
Restricción X > = Límite Superior

                                            ELEMENTOS DEL JUGO 
TIPO        | A% NARANJA  |  B% PLATANO   |  C% LECHE   |   D% ADITIVOS      |  COSTO TOTAL DEL CONTENIDO    |
PRODUCTO 1  |   10        |      12       |     8       |        4           |           $450/KG             |
PRODUCTO 2  |   8         |      15       |     11      |        2           |           $400/KG             |
PRODUCTO 3  |   12        |      12       |     7       |        7           |           $500/KG             |
PRODUCTO 4  |   10        |      10       |     10      |        5           |           $600/KG             |
PRODUCTO 5  |   15        |      6        |     10      |        10          |           $400/KG             |


"""

#Definimos el probelema este de de minimizar los costos de produccion 

from pulp import *
import pandas as pd 

problema = LpProblem("Minimazando los costos de produccion", LpMinimize)

#definimos las varables del problema 
x1 = LpVariable("x1", lowBound=0, cat= 'Continuous')
x2 = LpVariable("x2", lowBound=0, cat= 'Continuous')
x3 = LpVariable("x3", lowBound=0, cat= 'Continuous')
x4 = LpVariable("x4", lowBound=0, cat= 'Continuous')
x5 = LpVariable("x5", lowBound=0, cat= 'Continuous')

#Funcion objetivo 

problema += 450*x1 + 400*x2 + 500*x3 + 600*x4 + 400*x5

#Definimos las trestricciones 
#Limites superiores 
problema += 10*x1 +  8*x2 + 12*x3 + 10*x4 + 15*x5 <= 11, "NARANJA_SUP" #se le suma el 10% a cada restriccion 
problema += 12*x1 + 15*x2 + 12*x3 + 10*x4 +  6*x5 <= 13.5, "PLATANO_SUP"
problema +=  8*x1 + 11*x2 +  7*x3 + 10*x4 + 10*x5 <= 8.8 , "LECHE_SUP"
problema +=  5*x1 +  2*x2 +  7*x3 +  5*x4 + 10*x5 <= 5.5 , "ADITIVOS_SUP"

#Limites inferiores 
problema += 10*x1 +  8*x2 + 12*x3 + 10*x4 + 15*x5 >= 10 , "NARANJA_INF" #Se mantiene con los originales 
problema += 12*x1 + 15*x2 + 12*x3 + 10*x4 +  6*x5 >= 12 , "PLATANO_INF"
problema +=  8*x1 + 11*x2 +  7*x3 + 10*x4 + 10*x5 >= 8  , "LECHE_INF"
problema +=  5*x1 +  2*x2 +  7*x3 +  5*x4 + 10*x5 >= 5  , "ADITIVOS_INF"

# Restricción de que la suma de las proporciones debe ser 1 (100%)
problema += x1 + x2 + x3 + x4 + x5 == 1, "SUMA_PROPORCIONES"

#Se resuelve el problema
problema.solve()

# Imprimir el resultado
print("\nEstado:", LpStatus[problema.status])

print("\nCosto total de Produccion:", problema.objective.value())

print("\nValores óptimos de x1, x2, x3, x4, x5:")
for var in problema.variables():
    print(f"{var.name}: {var.value()}")

print()

sensibilidad = [{'Restricción ':i,'Precio Sombra': j.pi, 'Holgura': j.slack}
               for i, j in problema.constraints.items()]
print(pd.DataFrame(sensibilidad))



"""
=============================================================================
Respeustas de las preguntas 

1.¿Cuál sería la composición química del mix considerando los porcentajes 
obtenidos? (5 pts)

Respuesta:
Para determinar la composición química del mix, usamos los valores de las variables 
obtenidos tras resolver el modelo. 
Calculamos los porcentajes de cada componente (naranja, plátano, leche y aditivos) en la mezcla final.

Valores óptimos de x1, x2, x3, x4, x5:
x1: 0.62666667
x2: 0.21333333
x3: 0.053333333
x4: 0.0
x5: 0.10666667

En este caso la compocion quimica para el mix seria 0

NARANJA= 10*0.62666667 +  8*0.21333333 + 12*0.053333333 + 10*0.0 + 15*0.10666667 = 10.21% 
PLATANO= 12*0.62666667 + 15*0.21333333 + 12*0.053333333 + 10*0.0 +  6*0.10666667 = 12% 
LECHE=  8*0.62666667 + 11*0.21333333 +  7*0.053333333 + 10*0.0 + 10*0.10666667 = 8.8%  
ADITIVOS=  5*0.62666667 +  2*0.21333333 +  7*0.053333333 +  5*0.0 + 10*0.10666667 = 5% 

Por lo tanto para la composición química del mix seria de:
10.21% de naranja , 12% de Platano, 8.8% de leche y finalmente 5% de aditivos
==========================================================================================

2.¿Es posible reducir más el costo total del contenido de un 1 kg de mezcla? (2 pts)

Respuesta:
SI, Al observar los precios sombras del analisis de sensibilidad podemos ver que en la unidad de 
leche:sup tiene un resultado negativo, lo que indicaria que si aumentamos el rando superior 
se reduciria un mas el costo total de produccion mas -16.67 


=============================================================================================

3.¿Existe alguna restricción que tenga un exceso de material? (2 pts)
Respuesta:
Para determinar si alguna restricción tiene un exceso de material, debemos observar la "holgura" (slack) 
de cada restricción en la salida del análisis de sensibilidad. Si la holgura es mayor que cero, 
significa que hay exceso de material para esa restricción.

Entonces tenemos los siguientes resultados:
        Restricción   Precio Sombra   Holgura
0        NARANJA_SUP       0.000000  0.786667
1        PLATANO_SUP       0.000000  1.500000
2          LECHE_SUP     -16.666667 -0.000000
3       ADITIVOS_SUP       0.000000  0.500000
4        NARANJA_INF       0.000000 -0.213333
5        PLATANO_INF      16.666667 -0.000000
6          LECHE_INF       0.000000 -0.800000
7       ADITIVOS_INF      16.666667 -0.000000

Obserbamos que en:
NARANJA_SUP tenemos una holgura de 0.786667
PLATANO_SUP tenemos uan holgura de 1.500000
ADITIVOS_SUP tenemos uan holgura de 0.500000

significa que HAY un exeso de material en estas restricciones mencionadas anteriormente.
=============================================================================================

4.¿Qué ocurre si se aumenta en una unidad el límite inferior del porcentaje de plátano 
disponible?, ¿Es beneficioso o no para la empresa? (5 pts) 

Costo total de Produccion: 453.33333215000005

Valores óptimos de x1, x2, x3, x4, x5:
x1: 0.026666667
x2: 0.41333333
x3: 0.52
x4: 0.0
x5: 0.04

        Restricción   Precio Sombra   Holgura
0        NARANJA_SUP       0.000000  0.586667
1        PLATANO_SUP       0.000000  0.500000
2          LECHE_SUP     -16.666667 -0.000000
3       ADITIVOS_SUP       0.000000  0.500000
4        NARANJA_INF       0.000000 -0.413333
5        PLATANO_INF      16.666667 -0.000000
6          LECHE_INF       0.000000 -0.800000
7       ADITIVOS_INF      16.666667 -0.000000

Analizamos el problblema haciendo un aumento en la restriccion señalada 

Lo que ocurre al aumentar una unidad en el limite inferior del porcentaje de platano es que
el costo total de Produccion muestra un leve aumento de un 3.89% siendo de $436 a $453 siendo de $17,
hace tambien una disminucion en la varible de la naranja, disminuye la holgura de 0,1,4,7 del analisis de sencibilidad
por lo que No es beneficioso para la empresa. 

"""

