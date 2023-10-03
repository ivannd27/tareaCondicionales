edad = int(input("Edad:"))
ingresos = int(input("Ingresos:"))

def ejercicio7 (edad, ingresos):
    if (edad > 16 and ingresos > 1000):
        print("A pagar")
    else:
        print("No pagas")

ejercicio7(edad, ingresos)