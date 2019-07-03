# -*- coding: utf-8 -*-
import operaciones.op_bas as op
import menu_operaciones as mo

def calculadora():

    while True:
        opcion = mo.menu()

        if(opcion == 0):
            print("\nAdioooooos")
            break

        a = eval(input("Introduzca el primer número: "))
        b = eval(input("Introduzca el segundo número: "))

        if(opcion == 1):
            print("\nLa suma es:",op.sumar(a, b))
        elif(opcion == 2):
            print("\nLa resta es:",op.restar(a, b))
        elif(opcion == 3):
            print("\nEl producto es:",op.multiplicar(a, b))
        else:
            print("\nLa división es:",op.dividir(a, b))


calculadora()
