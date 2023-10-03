def ejercicio4 (a, b, c):
    if (a > b and a > c):
        print("a es el mayor de todos")
    elif (b > a and b > c):
        print("b es el mayor de todos")
    else:
        print("c es el mayor de todos")

a = int(input("¿cuanto es a? :"))
b = int(input("¿cuanto es b? :"))
c = int(input("¿cuanto es c? :"))

ejercicio4(a, b, c)