"""
Enunciado: 
cra un menu que sea capaz de guardar el nombre, edad,
y notas de cada estudiante que el usuario desee ingresar,
y que sea capaz de mostrar todos los usuarios, con su edad, notas 
y el promedio de notas por cada alumno, y el promedio de notas de todos los alumnos

"""

Estudiantes = []

def ingreso_alumnos():
    while True:
        try:
            nombre = str(input("ingrese el nombre del estudiante: "))
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

        except ValueError:
            print("Error, ingresar nuevamente")
            continue

        break
    
    

def registro_alumnos():
    if not Estudiantes:
        print("No hay estudiantes registrados.")
        return
    
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

def main():
    while True:
        try:
            #Creamos el menu de entrada que permitira mostrar las opciones al usuario
            print(""" 
                ======= Menu de Registro de Estudiantes =======
                1. Registrar Estudiantes.
                2. Mostrar todos los Estudiantes.
                3. Salir.
                """)
                       
            opcion= int(input("Ingrese una opción: "))
            
            if opcion == 1:
                ingreso_alumnos()              
                
            elif opcion == 2:
                registro_alumnos()
            
                continue  
            
            elif opcion == 3:
                break
            else:
                print("Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("Error. Ingrese opcion valida.")

if __name__ == '__main__':
    main()
