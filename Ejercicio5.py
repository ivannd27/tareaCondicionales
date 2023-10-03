dia = input("¿Que dia es? :")

def ejercicio5 (dia):
    if (dia == "lunes"):
        print("Hombro")
    
    elif (dia == "viernes"):
        print("Espalda y biceps")
    
    elif (dia == "sabado" or dia == "domingo"):
        print("se descansa")
        
    else:
        print("Aprende lo que te toca")

ejercicio5(dia)