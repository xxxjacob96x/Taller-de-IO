#definir nuestras variables 
#estamos hacindo mcion a lo que va a entrar a procesar 

while True:
    print("====Calculo de notas de estudiantes=== ")
    print("opcion 1( seguir)")
    print("opcion 2 (salir)")

    opcion=input("seleccione una opcion: ")

    if opcion=='1':

        C1=float(input("Ingrese calificasion 1: "))
        C2=float(input("Ingrese calificasion 2: "))
        C3=float(input("Ingrese calificasion 3: "))
        C4=float(input("Ingrese calificasion 4: "))

        #Para procesar la informacion de estos, hago:

        suma= C1+C2+C3+C4

        promedio= suma/4

        if promedio>=4:
            print("el promedoi de estudiante es: ", promedio)
            print("Situacion actual: ==Aprobado==")

        else:
            print("su calificasion fue: ", promedio)
            print("Estado delestudiantes: ==Reprobado==")
            
    elif opcion=='2':
        print("saliendo...")
        
        break
