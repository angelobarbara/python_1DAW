def main():
    a = int(input("Introduzca un numero entero mayor que cero: "))
    while a <= 0:
        int(input("Introduzca un numero entero mayor que cero: "))
    mi_lista = []
    for b in range (a):
         mi_lista += [int(input("Introduzca un numero entero: "))]
    print(mi_lista)


main()