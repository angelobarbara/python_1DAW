def main():
    mi_lista = ["hola","soy","angelo","angelo","adios"]
    cadena = str(input("Introduzca una cadena: "))

    if cadena in mi_lista:
        print("La cadena se encuentra en la lista y aparece", str(mi_lista.count(cadena)), "vez")

        cadena2 = str(input("Introduzca otra cadena: "))

        for a in range(len(mi_lista)):
            if mi_lista[a] == cadena:
                mi_lista[a] = cadena2

        print(mi_lista)

        for a in range(mi_lista.count(cadena2)):
            mi_lista.remove(cadena2)

        print(mi_lista)
    else:
       print("La cadena no se encuentra en la lista")

main()