"""
Enunciado: 
cra un menu que sea capaz de guardar el nombre, edad,
y notas de cada estudiante que el usuario desee ingresar,
y que sea capaz de mostrar todos los usuarios, con su edad, notas 
y el promedio de notas por cada alumno, y el promedio de notas de todos los alumnos

"""
#Definimos una base de datos en este caso de estudinates

Estudiantes = []

"""Ahora que definimos la BD (que es una lista)
comenzamos a realizar el ciclo while para hacer programa que permitira 
hacer el menu solicitado """

while True:
    #Creamos el menu de entrada que permitira mostrar las opciones al usuario
    print(""" 
          ======= Menu de Registro de Estudiantes =======
          1. Registrar Estudiantes.
          2. Mostrar todos los Estudiantes.
          3. Salir.
          """)
    
    #ahora definimos la variable opcion para que este pueda acceder con una opcion

    opcion= int(input("Ingrese una opción: "))
    
    if opcion == 1:
        nombre = input("ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        notas = [] #Aqui iniciamos la lista de notas 
        cantidad_notas = int(input("Ingrese la cantidad de notas: "))
        #Bucle para ingresar las notas del estudiante 
        for i in range(cantidad_notas):
            nota = float(input("ingrese una nota: "))
            #Agregamos la nota a la lista notas 
            notas.append(nota)
            alumno = (nombre, edad, notas)
        Estudiantes.append(alumno)

    elif opcion == 2:
        print("\n=== Lista de Estudiantes===" )
        #Inicializar la variable sumanota_total en 0 para luego ir sumandola por cada alumno 
        sumanota_total = 0
        #se inicia el bucle for 
        for estudiante in Estudiantes:

            nombre = estudiante[0]
            edad = estudiante[1]
            notas = estudiante[2]
            promedio_notas_alumno = sum(notas) / len(notas)
            #suma el promedio de cada alumno en sumanota_total 
            sumanota_total += promedio_notas_alumno
            print("") 
            # este nos sirve para mostrar en pantalla la info de cada alumno 
            print("Nombre:", nombre, "Edad:" , edad, "Notas:", notas, "Promedio:", promedio_notas_alumno)
        
        promedio_total = sumanota_total/len(Estudiantes)
        print("")
        print("El promedio de notas total de los estudiantes es: ", promedio_total)
    
    elif opcion == 3:
        break
    else:
        print("Opcion no valida. Intente nuevamente.")



    




#Obserbaciones 

""" 
El problema principal que se puede presentar en el código está en la comparación de la opción ingresada (opcion) 
con cadenas de texto ('1', '2', '3'). 
En la línea if opcion == '1':, estás comparando opcion, que es un entero, con una cadena de texto que representa el número 1. 
Esto causa que el bloque de código dentro de if opcion == '1': nunca se ejecute porque opcion nunca será igual a '1' como cadena de texto 
cuando el usuario ingresa 1 como entero.

Para corregirlo, simplemente cambiamos las comparaciones de cadenas por comparaciones de números enteros.

========== o ===========

El \n es un carácter especial que representa un salto de línea en Python y en muchos otros lenguajes de programación. 
Cuando se imprime en la consola o en un archivo de texto, \n hace que el texto siguiente se coloque en una nueva línea. 

En lo qye hicimos, utilizamos \n en las cadenas de texto dentro de las funciones print para crear líneas en blanco y
mejorar la legibilidad de la salida en la consola.

Por ejemplo, en esta parte de mi código tenemos que:

print("\n=== Lista de Estudiantes===" )   ===> esto queda el el codigo de mas arriba 

La cadena "\n=== Lista de Estudiantes===" hará que la línea "=== Lista de Estudiantes===" se imprima en una nueva línea, 
dejando una línea en blanco antes de mostrar la lista de estudiantes. 
Esto ayuda a separar visualmente las secciones de salida y hace que sea más fácil para el usuario leer la información presentada.

En resumen, \n es un carácter especial utilizado en cadenas de texto para representar un salto de línea 
y crear líneas en blanco en la salida de texto.



======== o ========
Ahora tambein en este codigo que programe se tiene que en el ultimo else se esta redirigiendo un mensaje de manera bucle para 
que este pueda hacer una nueva consulta y seguir con lo programadao jejeje Xd

"""
    