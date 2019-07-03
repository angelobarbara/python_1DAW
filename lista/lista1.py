def main():
    mi_lista = []

    num = eval(input("Introduzca un número positivo para seguir o un número negativo para salir: "))

    while num >= 0:

        mi_lista += [num]
        num = eval(input("Introduzca un número positivo para seguir o un número negativo para salir: "))

    print("El valor maximo es:",max(mi_lista))
    print("Números pares introducidos: ")
    for a in range(len(mi_lista)):
        if mi_lista[a]%2 == 0:
            print(mi_lista[a], end = " ")

main()