#Iniciamos con l lectura de informacion 

A = float(input("Ingrese A: "))
B = float(input("Ingrese B: "))
C = float(input("Ingrese C: "))

if A > B:
    if A > C:

        M=A
        print("El valor mayor es el de A, con: ",  M , "Como resultado")
    else:
        M =C
        print("El valor mayor es el de C, con: ",  M , "Como resultado")
else:
    if B>C:
        M =B
        print("El valor mayor es el de B, con: ",  M , "Como resultado")
    else:
        M=C
        print("El valor mayor es el de C, con: ",  M , "Como resultado")



