def main():
    a = int(input("Introduzca un numero entero: "))
    b = int(input("Introduzca otro numero entero: "))

    if b == 0:
        print("No se puede dividir por cero")
    elif a%b != 0:
        print("La division no es exacta")
    else:
        c = a/b
        print ("El resultado es",c)


main()