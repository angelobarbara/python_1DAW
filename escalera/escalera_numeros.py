# -*- coding: utf-8 -*-

def main():

    num1 = int(input("Escriba el primer número: "))
    num2 = int(input("Escriba el segundo número distinto del primero: "))
    num3 = int(input("Escriba el tercer número distinto del segundo: "))

    while num1 == num2:
        print("No ha escrito números válidos")
        num2 = int(input("Escriba el segundo número distinto del primero: "))

    mi_lista = []
    if num1 < num2:
        mi_lista += (list(range(num1, num2)))
    else:
        mi_lista += (list(range(num1, num2, -1)))

    if num2 < num3:
        mi_lista += (list(range(num2, num3 + 1)))
    else:
        mi_lista += (list(range(num2, num3 - 1, -1)))

    print(mi_lista)


main()