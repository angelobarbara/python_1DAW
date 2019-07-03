def main():
    a = int(input("Introduzca el numero de palabras en la lista: "))
    while a <= 0:
        int(input("Introduzca un numero entero mayor que cero: "))

    mi_lista = []
    for i in range(a):
        mi_lista += [input("Introduzca una palabra: ")]
    print("La lista creada es:", mi_lista)


main()