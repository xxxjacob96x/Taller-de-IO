""" Cree un menu que sea capaz de guardar 
el nombre, edad y notas de cada estudiante que el usuario desee ingresar,
y que sea capaz de mostrar todos los usuarios, con su edad, notas
y su promedio de notas por cada alumno,
y el promedio de notas de todos los alumnos. """

estudiantes = [("Jacob", 26, [7,5,4]), ("Camila", 24, [7,4,6])]

while True:
    print("""
        ====== Gestor de Alumnos ======
          1) Ingresar Alumnos 
          2) Mostrar Alumnos 
          Escariba "Salir" para finalizar el Programa 
        """)
    opcion = input("Ingrese una Opción: ")

    if opcion == "1": # Ingresar Usuarios 
        nombre = input("ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        notas = [] 
        cantidadnotas = int(input("Ingrese la cantidad de notas: "))

        for i in range(cantidadnotas):
            nota = float(input("ingrese una nota: "))
            notas.append(nota)
        alumno = (nombre, edad, notas)
        estudiantes.append(alumno)
    
    elif opcion == "2": # Mostrara todo los estudiantes 
        print("==========Lista de Estudiantes ===========")
        suma_promedios = 0
        for estudiante in estudiantes:
            nombre = estudiante[0]
            edad = estudiante[1]
            notas = estudiante[2]
            promedio = sum(notas)/ len(notas)
            suma_promedios += promedio 
            print("Nombre: ", nombre, "/ Edad: ", edad, "/ Notas ", notas, "/ Su promedio es: ", promedio)
        #Fin del bucle For 
        promedio_total = suma_promedios/ len(estudiantes)
        print("")
        print("El promedio total de los estudiantes fue: ", promedio_total)
    else:
        break
print("Saliendo......")


# Obserbaciones 
""" append es un método en Python que se usa para agregar un elemento al final de una lista. 
En el contexto de esta programacion, la línea estudiantes.append(alumno) está utilizando append para 
agregar una tupla llamada alumno al final de la lista estudiantes.

por lo tanto Aquí está cómo funciona:

estudiantes es una lista que contiene tuplas. Cada tupla representa la información de un estudiante, como su nombre, edad y notas.
alumno es una tupla que contiene la información de un estudiante específico que el usuario ingresa mediante la interacción con el programa.
Cuando se ejecuta estudiantes.append(alumno), Python agrega la tupla alumno al final de la lista estudiantes, lo que significa 
que ahora estudiantes contiene un estudiante más en su lista.

En resumen, append se utiliza para agregar elementos a una lista en Python, y en lo que programamos, se utiliza para agregar 
información de nuevos estudiantes a la lista de estudiantes existente.

entonces si nos preguntacen l dia de mañana, si sabemos agregar datos a una base de lista, les diremos que con la 
funcion append se puede

==================== o ==========================

La función len en Python se utiliza para obtener la longitud de un objeto iterable, como una lista, una tupla, 
un conjunto, una cadena de texto o un diccionario. La longitud se refiere al número de elementos que contiene el objeto iterable.

Por ejemplo:

Para una lista, len(lista) devolverá el número de elementos en la lista.
Para una cadena de texto, len(cadena) devolverá la cantidad de caracteres en la cadena.
Para una tupla, len(tupla) devolverá la cantidad de elementos en la tupla.
Para un conjunto, len(conjunto) devolverá la cantidad de elementos en el conjunto.
Para un diccionario, len(diccionario) devolverá la cantidad de pares clave-valor en el diccionario.

En el contexto de lo que programamos, usamos len para obtener la cantidad de notas que un estudiante tiene, como en esta línea:

cantidadnotas = int(input("Ingrese la cantidad de notas: "))

Y luego, más adelante, calculamos el promedio de notas
utilizando len para obtener la cantidad de notas que tiene cada estudiante:

promedio = sum(notas)/ len(notas)

En este caso, len(notas) devuelve la cantidad de elementos en la lista notas, 
que representan las notas del estudiante. 
La función len es muy útil para obtener información sobre la estructura 
y la cantidad de elementos en objetos iterables en Python.


"""