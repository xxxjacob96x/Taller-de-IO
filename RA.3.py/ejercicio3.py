A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

if A > B:
    if A > C: 
        M= A
        print("El Valor mayor es A, con  ", M, "Como resultado")
        
    else:
        M=C 
        print("El Valor mayor es C, con  ", M, "Como resultado")

elif B>C:
    M=B
    print("El Valor mayor es B, con  ", M, "Como resultado")
else:
    M=C
    print("El Valor mayor es C, con  ", M, "Como resultado")



