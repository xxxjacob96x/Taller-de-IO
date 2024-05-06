def es_nombre_valido(nombre):
    return all(c.isalpha() or c.isspace() for c in nombre)

Estudiantes = []

def ingreso_alumnos():
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ")
            if not es_nombre_valido(nombre):
                raise ValueError("El nombre debe contener solo letras y espacios.")

            # Preguntar al usuario si está seguro del nombre ingresado
            confirmacion = input(f"¿Estás seguro de que '{nombre}' es el nombre correcto? (s/n): ")
            if confirmacion.lower() != 's':
                raise ValueError("Nombre no confirmado.")

            edad = int(input("Ingrese la edad del estudiante: "))
            notas = []  # Aquí iniciamos la lista de notas 
            cantidad_notas = int(input("Ingrese la cantidad de notas: "))
            
            # Bucle para ingresar las notas del estudiante 
            for i in range(cantidad_notas):
                nota = float(input("Ingrese una nota: "))
                # Agregamos la nota a la lista notas 
                notas.append(nota)
                
            alumno = (nombre, edad, notas)
            Estudiantes.append(alumno)

        except ValueError as e:
            print("Error:", e)
            continue
        
        break

def registro_alumnos():
    if not Estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n=== Lista de Estudiantes ===" )
    # Inicializar la variable sumanota_total en 0 para luego ir sumándola por cada alumno 
    sumanota_total = 0
    # Se inicia el bucle for 
    for estudiante in Estudiantes:
        nombre = estudiante[0]
        edad = estudiante[1]
        notas = estudiante[2]
        promedio_notas_alumno = sum(notas) / len(notas)
        # Suma el promedio de cada alumno en sumanota_total 
        sumanota_total += promedio_notas_alumno
        print("") 
        # Este nos sirve para mostrar en pantalla la información de cada alumno 
        print("Nombre:", nombre, "Edad:" , edad, "Notas:", notas, "Promedio:", promedio_notas_alumno)

    promedio_total = sumanota_total / len(Estudiantes)
    print("")
    print("El promedio de notas total de los estudiantes es:", promedio_total)

def main():
    while True:
        try:
            # Creamos el menú de entrada que permitirá mostrar las opciones al usuario
            print(""" 
                ======= Menu de Registro de Estudiantes =======
                1. Registrar Estudiantes.
                2. Mostrar todos los Estudiantes.
                3. Salir.
                """)
                       
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1:
                ingreso_alumnos()              
                
            elif opcion == 2:
                registro_alumnos()
                continue  
            
            elif opcion == 3:
                
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Error. Ingrese una opción válida.")

if __name__ == '__main__':
    main()
