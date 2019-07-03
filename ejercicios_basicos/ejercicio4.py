def main(caracter):
    ancho = int(input("Introduzca la anchura del rectangulo: "))
    while ancho <= 0 and ancho >10:
        ancho = int(input("Introduzca la anchura del rectangulo: "))

    alto = int(input("Introduzca la altura del rectangulo: "))
    while alto <= 0 and alto >10:
        alto = int(input("Introduzca la altura del rectangulo: "))

    for c in range (alto):
        for j in range (ancho):
            print(caracter, end="")
        print()

    for d in range (alto * ancho):
        if d%ancho == 0:
            print()
        print(caracter, end="")


main("*")