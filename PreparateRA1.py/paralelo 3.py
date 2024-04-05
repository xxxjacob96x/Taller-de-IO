
while True:
    print("""=====Calculo de las notas====
        # Opcion 1 /Continuar) 
        # Opcion 2 /(Salir) """)
    
    opcion =input("Seleccione una opcion: ")

    if opcion=='1': 
        C1=float(input("Ingrese calificasion 1: "))
        C2=float(input("Ingrese calificasion 2: "))
        C3=float(input("Ingrese calificasion 3: "))
        C4=float(input("Ingrese calificasion 4: "))
        
        alumno=str(input("Ingrese el nombre del alumno: "))

        suma= C1+C2+C3+C4

        promedio= suma/4

        if promedio >=4:
            print("Nombre del Alumno: ", alumno)
            print("El promedio del estudiante es: ", promedio)
            print("Situacion actual: ==Aprobado==")
        else:
            print("Nombre del Alumno: ", alumno)
            print("su calificasion fue: ", promedio)
            print("Situacion Actual: ==Reprobado==")
    
    elif opcion =='2': 
        print("saliendo......")

        break

