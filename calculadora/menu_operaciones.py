# -*- coding: utf-8 -*-
def menu():
    print("\nSeleccione opción:\n",
          "1. Sumar\n",
          "2. Restar\n",
          "3. Multiplicar\n",
          "4. Dividir\n",
          "0. Salir")
    opcion = eval(input())
    while(opcion < 0 or opcion > 4):
        print("Itroduzca una opción válida\n")
        opcion = int(input())

    return opcion
